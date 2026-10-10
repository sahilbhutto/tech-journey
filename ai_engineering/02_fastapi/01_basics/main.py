
from fastapi import FastAPI, Depends, HTTPException # type: ignore
from sqlalchemy import create_engine, Column, Integer, String, Float # type: ignore
from sqlalchemy.orm import sessionmaker, declarative_base, Session # type: ignore

app = FastAPI()

# Database configuration
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


# Product model
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String, default="")


# Create database tables
Base.metadata.create_all(bind=engine)


# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Get all products
@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()


# Get one product
@app.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


# Create a product
@app.post("/products")
def create_product(
    name: str,
    price: float,
    description: str = "",
    db: Session = Depends(get_db)
):
    product = Product(
        name=name,
        price=price,
        description=description
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


# Update a product
@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    name: str,
    price: float,
    description: str = "",
    db: Session = Depends(get_db)
):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.name = name
    product.price = price
    product.description = description

    db.commit()
    db.refresh(product)

    return product


# Delete a product
@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()

    return {"message": "Product deleted successfully"}
