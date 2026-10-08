from __future__ import annotations

import asyncio
import json
import logging
import random
import time
from dataclasses import asdict, dataclass, field
from functools import wraps
from pathlib import Path
from typing import Any, Callable, Iterable, Iterator, Literal

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
logger = logging.getLogger("advanced_inventory")


class InventoryError(Exception):
    pass


class ProductNotFoundError(InventoryError):
    pass


class InsufficientStockError(InventoryError):
    pass


def retry(times: int = 3, delay: float = 0.2):
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_error: Exception | None = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    last_error = exc
                    logger.warning("Retry %s/%s for %s failed: %s", attempt, times, func.__name__, exc)
                    if attempt < times:
                        time.sleep(delay)
            raise last_error

        return wrapper

    return decorator


def timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        logger.info("%s ishladi: %.4f soniya", func.__name__, elapsed)
        return result

    return wrapper


@dataclass(slots=True)
class Product:
    sku: str
    name: str
    price: float
    stock: int = 0
    category: str = "misc"

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Product":
        return cls(**data)


class StorageStrategy:
    def save(self, data: dict[str, Any], path: Path) -> None:
        raise NotImplementedError

    def load(self, path: Path) -> dict[str, Any]:
        raise NotImplementedError


class JsonStorageStrategy(StorageStrategy):
    def save(self, data: dict[str, Any], path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def load(self, path: Path) -> dict[str, Any]:
        if not path.exists():
            return {}
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)


class InventoryManager:
    def __init__(self, storage: StorageStrategy, file_path: str | Path):
        self.storage = storage
        self.file_path = Path(file_path)
        self._products: dict[str, Product] = {}
        self._load_from_disk()

    def _load_from_disk(self) -> None:
        raw = self.storage.load(self.file_path)
        for sku, product_data in raw.items():
            self._products[sku] = Product.from_dict(product_data)

    def _save_to_disk(self) -> None:
        payload = {sku: product.to_dict() for sku, product in self._products.items()}
        self.storage.save(payload, self.file_path)

    @timer
    def add_product(self, product: Product) -> None:
        if product.sku in self._products:
            raise InventoryError(f"{product.sku} SKU allaqachon mavjud")
        self._products[product.sku] = product
        self._save_to_disk()
        logger.info("Yangi mahsulot qo'shildi: %s", product.name)

    @timer
    def update_stock(self, sku: str, quantity: int, mode: Literal["add", "remove"] = "add") -> Product:
        if sku not in self._products:
            raise ProductNotFoundError(f"{sku} SKU topilmadi")

        product = self._products[sku]
        if mode == "add":
            product.stock += quantity
        else:
            if product.stock < quantity:
                raise InsufficientStockError(f"{sku} uchun yetarli stock yo'q")
            product.stock -= quantity

        self._save_to_disk()
        return product

    @timer
    def sell(self, sku: str, quantity: int) -> float:
        product = self._products.get(sku)
        if product is None:
            raise ProductNotFoundError(f"{sku} SKU topilmadi")
        if product.stock < quantity:
            raise InsufficientStockError(f"{sku} uchun yetarli stock yo'q")

        product.stock -= quantity
        total = product.price * quantity
        self._save_to_disk()
        logger.info("Sotildi: %s x %s = %.2f", product.name, quantity, total)
        return total

    def list_products(self) -> list[Product]:
        return sorted(self._products.values(), key=lambda p: p.name.lower())

    def report(self) -> dict[str, Any]:
        total_items = sum(product.stock for product in self._products.values())
        total_value = sum(product.price * product.stock for product in self._products.values())
        return {
            "products_count": len(self._products),
            "stock_units": total_items,
            "inventory_value": round(total_value, 2),
            "categories": sorted({p.category for p in self._products.values()}),
        }


class ProductGenerator:
    def __init__(self, categories: Iterable[str]):
        self.categories = list(categories)

    def generate(self, count: int) -> list[Product]:
        products: list[Product] = []
        for i in range(count):
            category = random.choice(self.categories)
            sku = f"{category[:3].upper()}-{random.randint(1000, 9999)}"
            products.append(
                Product(
                    sku=sku,
                    name=f"{category.title()} {random.choice(['Pro', 'Max', 'Lite', 'Ultra', 'X'])}{random.randint(1, 99)}",
                    price=round(random.uniform(5.0, 999.99), 2),
                    stock=random.randint(0, 250),
                    category=category,
                )
            )
        return products


@retry(times=3, delay=0.1)
def risky_operation(value: int) -> int:
    if value == 0:
        raise ValueError("noldan katta bo'lishi kerak")
    return 100 // value


async def async_worker(name: str, delay: float, queue: asyncio.Queue[str]) -> None:
    await asyncio.sleep(delay)
    await queue.put(f"{name} finished in {delay:.2f}s")


async def process_async_tasks() -> list[str]:
    queue: asyncio.Queue[str] = asyncio.Queue()
    tasks = [
        asyncio.create_task(async_worker("worker-1", 0.2, queue)),
        asyncio.create_task(async_worker("worker-2", 0.5, queue)),
        asyncio.create_task(async_worker("worker-3", 0.1, queue)),
    ]
    await asyncio.gather(*tasks)
    results: list[str] = []
    while not queue.empty():
        results.append(await queue.get())
    return results


if __name__ == "__main__":
    manager = InventoryManager(JsonStorageStrategy(), "inventory_data.json")

    generated = ProductGenerator(["electronics", "office", "home", "sport"]).generate(15)
    for product in generated:
        try:
            manager.add_product(product)
        except InventoryError as exc:
            logger.warning("Duplicate/invalid product: %s", exc)

    existing_electronics = next((product for product in manager.list_products() if product.category == "electronics"), None)
    if existing_electronics is None:
        existing_electronics = Product(
            sku="ELE-2304",
            name="Electronics Pro 01",
            price=150.0,
            stock=25,
            category="electronics",
        )
        manager.add_product(existing_electronics)

    target_sku = existing_electronics.sku
    manager.update_stock(target_sku, 50, mode="add")
    total = manager.sell(target_sku, 10)
    report = manager.report()

    logger.info("Umumiy savat qiymati: %.2f", report["inventory_value"])
    logger.info("Sotilgan summa: %.2f", total)

    try:
        risky_operation(0)
    except ValueError as exc:
        logger.error("Riskli amal xatoligi: %s", exc)

    async def demo_async():
        results = await process_async_tasks()
        logger.info("Async natijalar: %s", results)

    asyncio.run(demo_async())

    logger.info("Mahsulotlar ro'yxati:")
    for product in manager.list_products()[:5]:
        logger.info("- %s | stock=%s | price=%.2f | category=%s", product.name, product.stock, product.price, product.category)
