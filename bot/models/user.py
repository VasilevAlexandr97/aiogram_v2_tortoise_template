from tortoise import fields
from tortoise.models import Model


class User(Model):
    """
        Bot user model
    """

    id = fields.IntField(pk=True)
    telegram_id = fields.BigIntField()
    username = fields.CharField(max_length=64, null=True)
    first_name = fields.CharField(max_length=128)
    last_name = fields.CharField(max_length=128, null=True)

    class Meta:
        table = "bot_users"

    def __str__(self):
        return f"user {self.id} {self.user_id} {self.first_name}"
