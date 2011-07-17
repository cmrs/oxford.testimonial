from plone.app.folder.folder import ATFolderSchema

from Products.Archetypes import atapi
from Products.ATContentTypes.configuration import zconf
from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.validation import V_REQUIRED

TestimonialFolderSchema = ATFolderSchema.copy() + atapi.Schema((

))

TestimonialSchema = ATContentTypeSchema.copy() + atapi.Schema((

    atapi.ImageField(
        name='featureImage',
        languageIndependent=True,
        storage=atapi.AnnotationStorage(),
        swallowResizeExceptions=zconf.swallowImageResizeExceptions.enable,
        pil_quality=zconf.pil_config.quality,
        pil_resize_algo=zconf.pil_config.resize_algo,
        max_size=zconf.ATImage.max_image_dimension,
        sizes= {
            'large'   : (768, 768),
            'preview' : (400, 400),
            'mini'    : (200, 200),
            'thumb'   : (128, 128),
            'tile'    :  (64, 64),
            'icon'    :  (32, 32),
            'listing' :  (16, 16),
        },
        validators=(('isNonEmptyFile', V_REQUIRED),
                    ('checkImageMaxSize', V_REQUIRED)),
        widget=atapi.ImageWidget(
            label='Feature Image',
            label_msgid='KebleContent_label_featureImage',
            description='The feature image that appears in the bottom right corner of the home page. Please upload an image with the following dimensions: width 465px, height: variable.',
            description_msgid='KebleContent_help_featureImage',
            i18n_domain='KebleContent',
            show_content_type = False,
        ),
    ),

))
