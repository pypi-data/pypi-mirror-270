#  Pyrofork - Telegram MTProto API Client Library for Python
#  Copyright (C) 2022-present Mayuri-Chan <https://github.com/Mayuri-Chan>
#
#  This file is part of Pyrofork.
#
#  Pyrofork is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrofork is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrofork.  If not, see <http://www.gnu.org/licenses/>.

import os
import re
from typing import List

import pyrogram
from pyrogram import enums, raw, types, utils
from pyrogram.file_id import FileType

class SendStory:
    def _split(self, message, entities, *args, **kwargs):
        return message, entities

    async def send_story(
        self: "pyrogram.Client",
        privacy: "enums.StoriesPrivacy" = None,
        allowed_users: List[int] = None,
        denied_users: List[int] = None,
        allowed_chats: List[int] = None,
        denied_chats: List[int] = None,
        animation: str = None,
        photo: str = None,
        video: str = None,
        pinned: bool = None,
        protect_content: bool = None,
        caption: str = None,
        parse_mode: "enums.ParseMode" = None,
        caption_entities: List["types.MessageEntity"] = None,
        period: int = None
    ) -> "types.Story":
        """Send new story.

        .. include:: /_includes/usable-by/users.rst

        Note: You must pass one of following paramater *animation*, *photo*, *video*

        Parameters:
            animation (``str`` | ``BinaryIO``, *optional*):
                Animation to send.
                Pass a file_id as string to send a animation that exists on the Telegram servers,
                pass an HTTP URL as a string for Telegram to get a animation from the Internet,
                pass a file path as string to upload a new animation that exists on your local machine, or
                pass a binary file-like object with its attribute ".name" set for in-memory uploads.

            photo (``str`` | ``BinaryIO``, *optional*):
                Photo to send.
                Pass a file_id as string to send a photo that exists on the Telegram servers,
                pass an HTTP URL as a string for Telegram to get a photo from the Internet,
                pass a file path as string to upload a new photo that exists on your local machine, or
                pass a binary file-like object with its attribute ".name" set for in-memory uploads.

            video (``str`` | ``BinaryIO``, *optional*):
                Video to send.
                Pass a file_id as string to send a video that exists on the Telegram servers,
                pass an HTTP URL as a string for Telegram to get a video from the Internet,
                pass a file path as string to upload a new video that exists on your local machine, or
                pass a binary file-like object with its attribute ".name" set for in-memory uploads.

            privacy (:obj:`~pyrogram.enums.StoriesPrivacy`, *optional*):
                Story privacy.
                Defaults to :obj:`~pyrogram.enums.StoriesPrivacy.PUBLIC`

            allowed_chats (List of ``int``, *optional*):
                List of chat_id which participant allowed to view the story.

            denied_chats (List of ``int``, *optional*):
                List of chat_id which participant denied to view the story.

            allowed_users (List of ``int``, *optional*):
                List of user_id whos allowed to view the story.

            denied_users (List of ``int``, *optional*):
                List of user_id whos denied to view the story.

            pinned (``bool``, *optional*):
                if True, the story will be pinned.
                default to False.

            protect_content (``bool``, *optional*):
                Protects the contents of the sent story from forwarding and saving.
                default to False.

            caption (``str``, *optional*):
                Story caption, 0-1024 characters.

            parse_mode (:obj:`~pyrogram.enums.ParseMode`, *optional*):
                By default, texts are parsed using both Markdown and HTML styles.
                You can combine both syntaxes together.

            caption_entities (List of :obj:`~pyrogram.types.MessageEntity`):
                List of special entities that appear in the caption, which can be specified instead of *parse_mode*.

            period (``int``, *optional*):
                How long the story will posted, in secs.
                only for premium users.

        Returns:
            :obj:`~pyrogram.types.Story` a single story is returned.

        Example:
            .. code-block:: python

                # Send new photo story
                photo_id = "abcd12345"
                await app.send_story(photo=photo_id, caption='Hello guys.')

        Raises:
            ValueError: In case of invalid arguments.
        """
        # TODO: media_areas

        if privacy:
            privacy_rules = [types.StoriesPrivacy(type=privacy)]
        else:
            privacy_rules = [types.StoriesPrivacy(type=enums.StoriesPrivacy.PUBLIC)]

        if animation:
            if isinstance(animation, str):
                if os.path.isfile(animation):
                    file = await self.save_file(animation)
                    media = raw.types.InputMediaUploadedDocument(
                        mime_type=self.guess_mime_type(animation) or "video/mp4",
                        file=file,
                        attributes=[
                            raw.types.DocumentAttributeVideo(
                                supports_streaming=True,
                                duration=0,
                                w=0,
                                h=0
                            ),
                            raw.types.DocumentAttributeAnimated()
                        ]
                    )
                elif re.match("^https?://", animation):
                    media = raw.types.InputMediaDocumentExternal(
                        url=animation
                    )
                else:
                    media = utils.get_input_media_from_file_id(animation, FileType.ANIMATION)
            else:
                file = await self.save_file(animation)
                media = raw.types.InputMediaUploadedDocument(
                    mime_type=self.guess_mime_type(animation) or "video/mp4",
                    file=file,
                    attributes=[
                        raw.types.DocumentAttributeVideo(
                            supports_streaming=True,
                            duration=0,
                            w=0,
                            h=0
                        ),
                        raw.types.DocumentAttributeAnimated()
                    ]
                )
        elif photo:
            if isinstance(photo, str):
                if os.path.isfile(photo):
                    file = await self.save_file(photo)
                    media = raw.types.InputMediaUploadedPhoto(
                        file=file
                    )
                elif re.match("^https?://", photo):
                    media = raw.types.InputMediaPhotoExternal(
                        url=photo
                    )
                else:
                    media = utils.get_input_media_from_file_id(photo, FileType.PHOTO)
            else:
                file = await self.save_file(photo)
                media = raw.types.InputMediaUploadedPhoto(
                    file=file
                )
        elif video:
            if isinstance(video, str):
                if os.path.isfile(video):
                    file = await self.save_file(video)
                    media = raw.types.InputMediaUploadedDocument(
                        mime_type=self.guess_mime_type(video) or "video/mp4",
                        file=file,
                        attributes=[
                            raw.types.DocumentAttributeVideo(
                                supports_streaming=True,
                                duration=0,
                                w=0,
                                h=0
                            )
                        ]
                    )
                elif re.match("^https?://", video):
                    media = raw.types.InputMediaDocumentExternal(
                        url=video
                    )
                else:
                    media = utils.get_input_media_from_file_id(video, FileType.VIDEO)
            else:
                file = await self.save_file(video)
                media = raw.types.InputMediaUploadedDocument(
                    mime_type=self.guess_mime_type(video) or "video/mp4",
                    file=file,
                    attributes=[
                        raw.types.DocumentAttributeVideo(
                            supports_streaming=True,
                            duration=0,
                            w=0,
                            h=0
                        )
                    ]
                )
        else:
            raise ValueError("You need to pass one of the following parameter animation/photo/video!")
        
        text, entities = self._split(**await utils.parse_text_entities(self, caption, parse_mode, caption_entities))

        if allowed_chats and len(allowed_chats) > 0:
            chats = [await self.resolve_peer(chat_id) for chat_id in allowed_chats]
            privacy_rules.append(raw.types.InputPrivacyValueAllowChatParticipants(chats=chats))
        if denied_chats and len(denied_chats) > 0:
            chats = [await self.resolve_peer(chat_id) for chat_id in denied_chats]
            privacy_rules.append(raw.types.InputPrivacyValueDisallowChatParticipants(chats=chats))
        if allowed_users and len(allowed_users) > 0:
            users = [await self.resolve_peer(user_id) for user_id in allowed_users]
            privacy_rules.append(raw.types.InputPrivacyValueAllowUsers(users=users))
        if denied_users and len(denied_users) > 0:
            users = [await self.resolve_peer(user_id) for user_id in denied_users]
            privacy_rules.append(raw.types.InputPrivacyValueDisallowUsers(users=users))

        r = await self.invoke(
            raw.functions.stories.SendStory(
                media=media,
                privacy_rules=privacy_rules,
                random_id=self.rnd_id(),
                pinned=pinned,
                noforwards=protect_content,
                caption=text,
                entities=entities,
                period=period
            )
        )
        return await types.Story._parse(self, r.updates[0].story, r.updates[0].user_id)
