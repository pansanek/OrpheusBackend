from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app.models.post_model import CreatePostRequest
from app.models.post_model import Post
from app.services.post_service import PostService

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
            creator_id=post_info.creator_id,
            creatorName=post_info.creatorName,
            creatorPicture=post_info.creatorPicture,
            text=post_info.text,
            likes=post_info.likes,
            comments=post_info.comments,
            attachment=post_info.attachment,
            creator_type=post_info.creator_type,
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


@post_router.get('/creator/{id}')
def get_post_by_creator_id(id: UUID, post_service: PostService = Depends(PostService)) -> Post:
    try:
        post = post_service.get_post_by_creator_id(id)
        return post.dict()
    except KeyError:
        raise HTTPException(404, f'Post with id={id} not found')
