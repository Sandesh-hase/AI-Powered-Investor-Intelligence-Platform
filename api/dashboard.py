from fastapi import APIRouter

router = APIRouter()

@router.get('/dashboard')
def get_dashboard_data():
    return {
        'summary': {
            'revenue': '24.8M',
            'growth': '18%',
            'sentiment': 'Bullish'
        }
    }
