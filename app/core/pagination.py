from typing import Any, Dict

MAX_PAGE_SIZE = 100


def paginate(session, model: Any, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
    page_size = max(1, min(page_size, MAX_PAGE_SIZE))
    total_items = session.query(model).count()
    total_pages = (total_items + page_size - 1) // page_size if total_items else 1
    offset = (page - 1) * page_size
    items = session.query(model).offset(offset).limit(page_size).all()
    return {
        "items": items,
        "total_items": total_items,
        "total_pages": total_pages,
        "page": page,
        "page_size": page_size,
    }
