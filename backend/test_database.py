from database import engine, SessionLocal

try:
    # Test the actual database connection
    with engine.connect() as connection:
        print("Database connection successful!")

    # Test creating a session
    db = SessionLocal()
    print("Database session created successfully!")

    db.close()
    print("Database session closed successfully!")

except Exception as e:
    print("Database test failed:")
    print(e)