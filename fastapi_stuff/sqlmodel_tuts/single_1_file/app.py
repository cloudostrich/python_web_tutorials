from db_models import engine, Session, Hero, Team
from sqlmodel import select


def select_heroes():
    with Session(engine) as session:
        #statement = select(Hero)
        #results = session.exec(statement)
        #for hero in results:
        #    print(hero)
        print(session.exec(select(Hero)).all())


def select_hero():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name=="Deadpond")
        results = session.exec(statement)
        for hero in results:
            print(hero)


def update_hero():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name=="Spider-Boy")
        results = session.exec(statement)
        hero = results.one()
        print("Hero:", hero)

        hero.age = 16
        session.add(hero)
        session.commit()


def select_heroteam():
    with Session(engine) as session:
        statement = select(Hero, Team).where(Hero.id == Team.id)
        results = session.exec(statement)
        for hero, team in results:
            print("Hero:", hero, "Team:", team)


def select_by_join():
    with Session(engine) as session:
        statement = select(Hero, Team).join(Team, isouter=True)  #isouter: outerjoin
        results = session.exec(statement)
        for hero, team in results:
            print("Hero:", hero, "Team:", team)


def add2team():
    pass


def select_spidey_team():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        result = session.exec(statement)
        hero_spider_boy = result.one()

        # Code from the previous example omitted 👈

        print("Spider-Boy's team again:", hero_spider_boy.team)




def select_list_team():
    with Session(engine) as session:
        statement = select(Team).where(Team.name == "Preventers")
        result = session.exec(statement)
        team_preventers = result.one()

        print("Preventers heroes:", team_preventers.heroes)
        print("last:", team_preventers.heroes[-1])

if __name__ == "__main__":
    select_list_team()
