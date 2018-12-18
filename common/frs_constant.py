# -*- coding: utf-8 -*-

class FrsConstant(object):
    END_POINT = "https://face.cn-north-1.myhuaweicloud.com"
    REGION = "cn-north-1"
    SERVICE_QUERY_URI = "/v1/%s/subscribe"
    FACE_DETECT_URI = "/v1/%s/face-detect"
    FACE_COMPARE_URI = "/v1/%s/face-compare"
    FACE_SEARCH_URI = "/v1/%s/face-sets/%s/search"
    FACE_ADD_URI = "/v1/%s/face-sets/%s/faces"
    FACE_GET_RANGE_URI = "/v1/%s/face-sets/%s/faces?offset=%d&limit=%d"
    FACE_GET_ONE_URI = "/v1/%s/face-sets/%s/faces?face_id=%s"
    FACE_GET_BASE_URI = "/v1/%s/face-sets/%s/faces"
    FACE_DELETE_BY_EXTERNAL_IMAGE_ID_URI = "/v1/%s/face-sets/%s/faces?external_image_id=%s"
    FACE_DELETE_BY_FACE_ID_URI = "/v1/%s/face-sets/%s/faces?face_id=%s"
    FACE_DELETE_BY_FIELD_ID_URI = "/v1/%s/face-sets/%s/faces?%s=%s"
    FACE_SET_CREATE_URI = "/v1/%s/face-sets"
    FACE_SET_GET_ALL_URI = "/v1/%s/face-sets"
    FACE_SET_GET_ONE_URI = "/v1/%s/face-sets/%s"
    FACE_SET_DELETE_URI = "/v1/%s/face-sets/%s"
    LIVE_DETECT_URI = "/v1/%s/live-detect"
    FACE_QUALITY_URI = "/v1/%s/face/quality/face-quality"
    BLUR_CLASSIFY_URI = "/v1/%s/face/quality/blur-classify"
    HEAD_POST_ESTIMATE_URI = "/v1/%s/face/quality/head-pose-estimate"