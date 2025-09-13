##Database configuration
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./movies.db"

#creer un moteur de de base de donnees (engine) qui etablie la connexion avec notre base SQLITE (movies.db)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

#Definir une sessionLocal qui permet de creer des sessions pour interagir avec la base de donnees
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


#Definir Base, qui servira de classe de base pour nos modeles SQLAlchemy
Base = declarative_base()

#if __name__ == "__main__":
#    try:
#        with engine.connect() as connection:
#            print("Database connection successful.")
#    except Exception as e:
#        print(f"Database connection failed: {e}")