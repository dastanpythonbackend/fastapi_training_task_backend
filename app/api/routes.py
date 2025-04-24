from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
import httpx
from app.core.models import URLRequest
from app.utils.helper import generate_shorten_id

router = APIRouter()
url_mapping = {}


@router.post('/', status_code=201, tags=['URL Shortener'],
             summary='Get an abbreviated version of the transmitted URL.',
             description='The method accepts the URL string for shortening in '
                         'the request body and returns a response with the code 201.')
async def shorten_url(data: URLRequest):
    original_url = data.url.strip()
    if not original_url:
        raise HTTPException(status_code=400, detail='Empty URL')

    shorten_id = generate_shorten_id()
    url_mapping[shorten_id] = original_url
    return {'shorten_id': shorten_id}


@router.get('/morty', tags=['Rick and Morty'], summary='Get Morty character info',
            description='Make an async service request to the Rick and '
                        'Morty API and return selected character data.')
async def get_morty():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get('https://rickandmortyapi.com/api/character/2')
            data = response.json()
            return {
                'name': data['name'],
                'status': data['status'],
                'image': data['image'],
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get('/{shorten_id}', tags=['URL Shortener'], summary='Return the original URL.',
            description='The method takes the identifier of the shortened '
                        'URL as a parameter and returns a response with the '
                        'code 307 and the original URL in the Location header.')
async def redirect_url(shorten_id: str):
    original_url = url_mapping.get(shorten_id)
    if original_url:
        return RedirectResponse(url=original_url, status_code=307)
    raise HTTPException(status_code=404, detail='URL not found')
