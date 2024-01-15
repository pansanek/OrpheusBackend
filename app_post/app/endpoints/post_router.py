from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app_post.app.models.post_model import CreatePostRequest
from app_post.app.services.post_service import PostService
from app_post.app.models.post_model import Post

post_router = APIRouter(prefix='/posts', tags=['Posts'])

@post_router.get('/')
def get_posts(post_service: PostService = Depends(PostService)) -> list[Post]:
    return post_service.get_all_posts()

@post_router.post('/')
def create_post(
    post_info: CreatePostRequest,
    post_service: PostService = Depends(PostService)
) -> Post:
    try:
        post = post_service.create_post(
            user_id=post_info.user_id,
            caption=post_info.caption,
            image=post_info.image,
            creator_type=post_info.creator_type
        )
        return post.dict()
    except KeyError:
        raise HTTPException(400, f'Post with id={post_info.user_id} already exists')

@post_router.get('/{id}')
def get_post_by_id(id: UUID, post_service: PostService = Depends(PostService)) -> Post:
    try:
        post = post_service.get_post_by_id(id)
        return post.dict()
    except KeyError:
        raise HTTPException(404, f'Post with id={id} not found')