from sys import getsizeof

import orjson

from buz.event.transactional_outbox import OutboxRecord
from buz.event.transactional_outbox.outbox_record_validation.abstract_outbox_record_validator import (
    AbstractOutboxRecordValidator,
)
from buz.event.transactional_outbox.outbox_record_validation.outbox_record_size_not_allowed_exception import (
    OutboxRecordSizeNotAllowedException,
)


class SizeOutboxRecordValidator(AbstractOutboxRecordValidator):
    def __init__(self, size_limit_in_bytes: int = 1000000):
        self.__size_limit_in_bytes = size_limit_in_bytes
        super().__init__()

    def validate(self, record: OutboxRecord) -> None:
        size = getsizeof(orjson.dumps(record))
        if size >= self.__size_limit_in_bytes:
            raise OutboxRecordSizeNotAllowedException(
                record=record, size_limit_in_bytes=self.__size_limit_in_bytes, record_size=size
            )

        return super().validate(record)
