from fastapi import APIRouter

router = APIRouter()

@router.get('/search')
def search_insights(q: str):
    # TODO: implement search logic using vector search or database
    return {
        'query': q,
        'results': []
    }
