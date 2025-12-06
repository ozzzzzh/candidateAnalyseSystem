# 小红书网络结构分析
## 文章部分
### link1: api/sns/web/v1/user_posted
https://edith.xiaohongshu.com/api/sns/web/v1/user_posted?num=30&cursor=68f58db9000000000703493b&user_id=6246cc94000000001000d74b&image_formats=jpg,webp,avif&xsec_token=&xsec_source=

- Request参数分析
    - num : 分页数量
    - cursor：
    - user_id：用户ID(main key)
    - image_formats
    - xsec_token
    - xsec_source

- Response分析
    - raw code
    ``` json
        {
            "cover": {
                "trace_id": "",
                "info_list": [
                    {
                        "image_scene": "WB_PRV",
                        "url": "http://sns-webpic-qc.xhscdn.com/202512042225/764de437e2dc866df3ba10fd20bccf30/spectrum/1040g0k031nnjtbllku0g5oi6pia41lqb5l3mcc0!nc_n_webp_prv_1"
                    },
                    {
                        "image_scene": "WB_DFT",
                        "url": "http://sns-webpic-qc.xhscdn.com/202512042225/7c5861b97cd8751aa8759a7de2475c22/spectrum/1040g0k031nnjtbllku0g5oi6pia41lqb5l3mcc0!nc_n_webp_mw_1"
                    }
                ],
                "url_pre": "http://sns-webpic-qc.xhscdn.com/202512042225/764de437e2dc866df3ba10fd20bccf30/spectrum/1040g0k031nnjtbllku0g5oi6pia41lqb5l3mcc0!nc_n_webp_prv_1",
                "url_default": "http://sns-webpic-qc.xhscdn.com/202512042225/7c5861b97cd8751aa8759a7de2475c22/spectrum/1040g0k031nnjtbllku0g5oi6pia41lqb5l3mcc0!nc_n_webp_mw_1",
                "file_id": "",
                "height": 2022,
                "width": 1516,
                "url": ""
            },
            "note_id": "68f198940000000003019306",
            "xsec_token": "ABGxQZ3dmrl8zE-77xmJCB_jHVBbldREXIP1VZl0nmHNQ=",
            "type": "video",
            "display_title": "扫雷 | 重生之我在A股开超市，能赚多少钱？",
            "user": {
                "avatar": "https://sns-avatar-qc.xhscdn.com/avatar/6246cd25bc6d64731a37a464.jpg",
                "user_id": "6246cc94000000001000d74b",
                "nickname": "量化交易邢不行啊",
                "nick_name": "量化交易邢不行啊"
            },
            "interact_info": {
                "liked_count": "11",
                "sticky": false,
                "liked": false
            }
        },
    ```
- 各个字段解释
    - cover: 笔记封面信息
    - trace_id: 内部追踪 ID，用于日志或调试
    - info_list: 封面图片列表
        - image_scene: 图片类型或用途标识，例如 "WB_PRV"（预览图）、"WB_DFT"（默认图）
        - url: 图片 URL
    - url_pre: 封面图片预览 URL
    - url_default: 封面图片默认显示 URL
    - file_id: 图片文件 ID（可能用于内部管理）
    - height: 图片高度（像素）
    - width: 图片宽度（像素）
    - url: 备用 URL，通常为空
    - note_id: 笔记唯一标识符
    - xsec_token: 前端 JS 生成的安全签名，用于合法请求接口
    - type: 笔记类型，例如 "video"（视频笔记）、"normal"（图文笔记）
    - display_title: 笔记标题或显示文本
    - user: 作者信息
    - avatar: 作者头像 URL
    - user_id: 作者唯一 ID
    - nickname: 作者昵称，用于显示
    - nick_name: 作者昵称（兼容或内部字段）
    - interact_info: 用户交互信息
    - liked_count: 点赞数量
    - sticky: 是否置顶
    - liked: 当前登录用户是否已点赞

### link2: api/sns/web/v2/comment/page
https://edith.xiaohongshu.com/api/sns/web/v2/comment/page?note_id=68f1e55d0000000007001e14&cursor=&top_comment_id=&image_formats=jpg,webp,avif&xsec_token=ABGxQZ3dmrl8zE-77xmJCB_perW36IoK0VY13Nd0B_AME%3D

- Request参数分析
    - note_id : 笔记id
    - cursor：
    - top_comment_id：
    - image_formats
    - xsec_token

- Response分析
    - raw code
    ``` json
        {
        "code": 0,
        "success": true,
        "msg": "成功",
        "data": {
            "user_id": "680daab5000000000601fa6e",
            "comments": [
                {
                    "status": 0,
                    "show_tags": [],
                    "create_time": 1761090097000,
                    "sub_comment_count": "2",
                    "sub_comments": [
                        {
                            "content": "求公众号",
                            "show_tags": [],
                            "target_comment": {
                                "id": "68f81a300000000033005693",
                                "user_info": {
                                    "xsec_token": "ABuckxbvzABT96hao9RKlyc8e_P-PBOi9U1EV0hXhzSU8=",
                                    "user_id": "64291833000000001102003a",
                                    "nickname": "sqs",
                                    "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo30tkbc0ko4s005p1930pkc01q0nmjh30?imageView2/2/w/120/format/jpg"
                                }
                            },
                            "at_users": [],
                            "liked": false,
                            "like_count": "0",
                            "user_info": {
                                "user_id": "6049bb800000000001002423",
                                "nickname": "小红薯嘻嘻嘻",
                                "image": "https://sns-avatar-qc.xhscdn.com/avatar/6049bb9b588feb7fe34242a6.jpg?imageView2/2/w/120/format/jpg",
                                "xsec_token": "AB3GcJrKHVlJfKC61czCOjZMjbhg8ZzL7CnoxHtAs0lHE="
                            },
                            "create_time": 1761204991000,
                            "id": "68f9daff000000003900528d",
                            "note_id": "68f1e55d0000000007001e14",
                            "status": 0
                        }
                    ],
                    "sub_comment_cursor": "68f9daff000000003900528d",
                    "sub_comment_has_more": true,
                    "like_count": "0",
                    "content": "其实研报的数量也太多了 让人不知道从哪一天开始读起 可以把那些一线的金工的公众号关注了 推送的时候看看 有没有灵感[笑哭R]",
                    "at_users": [],
                    "id": "68f81a300000000033005693",
                    "note_id": "68f1e55d0000000007001e14",
                    "liked": false,
                    "user_info": {
                        "user_id": "64291833000000001102003a",
                        "nickname": "sqs",
                        "image": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo30tkbc0ko4s005p1930pkc01q0nmjh30?imageView2/2/w/120/format/jpg",
                        "xsec_token": "ABuckxbvzABT96hao9RKlyc8e_P-PBOi9U1EV0hXhzSU8="
                    }
                }
            ],
            "cursor": "68f81a300000000033005693",
            "has_more": false,
            "time": 1764907237464,
            "xsec_token": "AB6NXgb5QdzivQg1Hk8IY78A3bh04zYtkbko9Tb-xK7PE="
        }
    }
    ```

### link3: api/sns/web/v1/feed
这个应该是网页预览
- payload 参数
    ``` json
        {
        "source_note_id": "68f1e55d0000000007001e14",
        "image_formats": ["jpg", "webp", "avif"],
        "extra": { "need_body_topic": "1" },
        "xsec_source": "pc_user",
        "xsec_token": "ABGxQZ3dmrl8zE-77xmJCB_perW36IoK0VY13Nd0B_AME="
        }
    ``` 
- response 
    - raw data
    ``` json
        {
        "code": 0,
        "success": true,
        "msg": "成功",
        "data": {
            "cursor_score": "",
            "items": [
                {
                    "note_card": {
                        "image_list": [
                            {
                                "width": 932,
                                "info_list": [
                                    {
                                        "image_scene": "WB_PRV",
                                        "url": "http://sns-webpic-qc.xhscdn.com/202512051217/73f9bca40468296bd70f5848700e0b60/spectrum/1040g34o31nntenkqku105oi6pia41lqbl3hr23g!nd_prv_wlteh_webp_3"
                                    },
                                    {
                                        "image_scene": "WB_DFT",
                                        "url": "http://sns-webpic-qc.xhscdn.com/202512051217/9824f32dad3ba2a3bef626c82af6d685/spectrum/1040g34o31nntenkqku105oi6pia41lqbl3hr23g!nd_dft_wlteh_webp_3"
                                    }
                                ],
                                "url_pre": "http://sns-webpic-qc.xhscdn.com/202512051217/73f9bca40468296bd70f5848700e0b60/spectrum/1040g34o31nntenkqku105oi6pia41lqbl3hr23g!nd_prv_wlteh_webp_3",
                                "url_default": "http://sns-webpic-qc.xhscdn.com/202512051217/9824f32dad3ba2a3bef626c82af6d685/spectrum/1040g34o31nntenkqku105oi6pia41lqbl3hr23g!nd_dft_wlteh_webp_3",
                                "stream": {},
                                "file_id": "",
                                "height": 3633,
                                "url": "",
                                "trace_id": "",
                                "live_photo": false
                            }
                        ],
                        "tag_list": [
                            {
                                "name": "量化投资",
                                "type": "topic",
                                "id": "5e10285a00000000010035f1"
                            },
                            {
                                "id": "5be432abe772cd000136f832",
                                "name": "金融",
                                "type": "topic"
                            },
                            {
                                "type": "topic",
                                "id": "5bf56352e19216000115879c",
                                "name": "炒股"
                            },
                            {
                                "type": "topic",
                                "id": "6463903d000000002801b2d4",
                                "name": "学习"
                            },
                            {
                                "name": "编程",
                                "type": "topic",
                                "id": "5be6f604db601f0001f98c11"
                            },
                            {
                                "type": "topic",
                                "id": "5f70a874000000000100757c",
                                "name": "理财"
                            },
                            {
                                "id": "5d719540000000000103b788",
                                "name": "量化交易",
                                "type": "topic"
                            },
                            {
                                "id": "6463903d000000002801b2d4",
                                "name": "学习",
                                "type": "topic"
                            },
                            {
                                "id": "5c152b670000000003028cb7",
                                "name": "知识分享",
                                "type": "topic"
                            }
                        ],
                        "last_update_time": 1760683358000,
                        "share_info": {
                            "un_share": false
                        },
                        "user": {
                            "user_id": "6246cc94000000001000d74b",
                            "nickname": "量化交易邢不行啊",
                            "avatar": "https://sns-avatar-qc.xhscdn.com/avatar/6246cd25bc6d64731a37a464.jpg",
                            "xsec_token": "ABi5Lt9MgF3PVfTaz2Ogmnp0d9GXouzlEye6AW-wHgKKU="
                        },
                        "type": "normal",
                        "title": "不要翻大部头的书！  不要翻大部头的书！",
                        "desc": "#量化投资[话题]# #金融[话题]# #炒股[话题]# #学习[话题]# #编程[话题]# #理财[话题]##量化交易[话题]# #学习[话题]# #知识分享[话题]#",
                        "interact_info": {
                            "relation": "none",
                            "liked": false,
                            "liked_count": "7",
                            "collected": false,
                            "collected_count": "1",
                            "comment_count": "3",
                            "share_count": "0",
                            "followed": false
                        },
                        "at_user_list": [],
                        "time": 1760842831000,
                        "note_id": "68f1e55d0000000007001e14"
                    },
                    "id": "68f1e55d0000000007001e14",
                    "model_type": "note"
                }
            ],
            "current_time": 1764908264968
        }
    }
    ```
    - response formatted data
        - items: 笔记内容集合
        - note_card: 笔记主体内容结构
            - image_list: 笔记图片列表
            - url_default: 默认封面图
            - width/height: 图片尺寸
            - tag_list: 话题 / 标签列表
            - last_update_time: 最后更新时间
            - user: 作者信息
            - user_id: 作者ID
            - nickname: 昵称
            - avatar: 头像URL
            - type: 笔记类型（video/normal）
            - title: 笔记标题
            - desc: 正文描述（含话题格式文本）
            - interact_info:
            - liked_count: 点赞数
            - collected_count: 收藏数
            - comment_count: 评论数
            - share_count: 分享数

