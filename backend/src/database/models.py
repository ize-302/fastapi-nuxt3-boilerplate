from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Notes(models.Model):
    id = fields.IntField(pk=True)
    note = fields.CharField(max_length=150)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


Note_Pydantic = pydantic_model_creator(Notes, name='Note')
NoteIn_Pydantic = pydantic_model_creator(Notes, name='NoteIn', exclude_readonly=True)
