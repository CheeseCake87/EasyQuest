import random

from flask_bigapp.security import login_check

from .. import bp


@bp.get("/roll-dice")
@login_check('authenticated', 'auth.login')
def your_dice():
    # random dice roll
    roll = random.randint(1, 6)

    return {
        "roll": roll
    }
