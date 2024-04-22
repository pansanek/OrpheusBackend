from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException

from app_comment.app.models.comment_model import Comment, CreateCommentRequest
from app_comment.app.services.comment_service import CommentService

comment_router = APIRouter(prefix='/comments', tags=['Comments'])


@comment_router.get('/')
def get_comments(comment_service: CommentService = Depends(CommentService)) -> list[Comment]:
    return comment_service.get_all_comments()


@comment_router.post('/')
def create_comment(
        comment_info: CreateCommentRequest,
        comment_service: CommentService = Depends(CommentService)
) -> Comment:
    try:
        comment = comment_service.create_comment(
            user=comment_info.user,
            post_id=comment_info.post_id,
            text=comment_info.text,
            timestamp=comment_info.timestamp
        )
        return comment.dict()
    except KeyError:
        raise HTTPException(400,
                            f'Comment with user_id={comment_info.user_id} and post_id={comment_info.post_id} already exists')


@comment_router.get('/{id}')
def get_comment_by_id(id: UUID, comment_service: CommentService = Depends(CommentService)) -> Comment:
    try:
        comment = comment_service.get_comment_by_id(id)
        return comment.dict()
    except KeyError:
        raise HTTPException(404, f'Comment with id={id} not found')



@comment_router.put('/{comment_id}')
def update_comment(
        comment_id: UUID,
        comment_info: CreateCommentRequest,
        comment_service: CommentService = Depends(CommentService)
) -> Comment:
    try:
        updated_comment = comment_service.update_comment(
            comment_id=comment_id,
            user=comment_info.user,
            post_id=comment_info.post_id,
            text=comment_info.text,
            timestamp=comment_info.timestamp
        )
        return updated_comment
    except KeyError:
        raise HTTPException(404, f'Comment with id={comment_id} not found')