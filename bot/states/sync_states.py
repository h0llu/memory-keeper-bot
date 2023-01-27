from aiogram.fsm.state import State, StatesGroup


class Sync(StatesGroup):
    synching = State()
    not_synching = State()
