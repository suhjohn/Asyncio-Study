import aiopg.sa
import sqlalchemy as sa

from sanic_study.main import app

meta = sa.MetaData()

question = sa.Table(
    'question', meta,
    sa.Column('id', sa.Integer, nullable=False),
    sa.Column('question_text', sa.String(200), nullable=False),
    sa.Column('pub_date', sa.Date, nullable=False),

    sa.PrimaryKeyConstraint('id', name='question_id_pkey')
)


choice = sa.Table(
    'choice', meta,
    sa.Column('id', sa.Integer, nullable=False),
    sa.Column('question_id', sa.Integer, nullable=False),
    sa.Column('choice_text', sa.String(200), nullable=False),
    sa.Column('votes', sa.Integer, server_default="0", nullable=False),

    sa.PrimaryKeyConstraint('id', name='choice_id_pkey'),
    sa.ForeignKeyConstraint(['question_id'], [question.c.id],
                            name='choice_question_id_fkey',
                            ondelete='CASCADE')
)

async def init_pg(app):
    conf = app['config']
    engine = await aiopg.sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
        minsize=conf['minsize'],
        maxsize=conf['maxsize'])
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()


app.on_cleanup.append(close_pg)
