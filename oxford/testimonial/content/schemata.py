from plone.app.folder.folder import ATFolderSchema

from Products.Archetypes.atapi import AnnotationStorage
from Products.Archetypes.atapi import ImageField
from Products.Archetypes.atapi import ImageWidget
from Products.Archetypes.atapi import RichWidget
from Products.Archetypes.atapi import StringWidget
from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import TextField
from Products.ATContentTypes import ATCTMessageFactory as _
from Products.ATContentTypes.configuration import zconf
from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.ATContentTypes.content.schemata import finalizeATCTSchema
from Products.validation import V_REQUIRED

TestimonialFolderSchema = ATFolderSchema.copy() + Schema((

))

TestimonialSchema = ATContentTypeSchema.copy() + Schema((

    TextField('text',
        required = False,
        searchable = True,
        primary = True,
        storage = AnnotationStorage(migrate=True),
        validators = ('isTidyHtmlWithCleanup',),
        default_output_type = 'text/x-html-safe',
        widget = RichWidget(
            description = '',
            label = 'Testimonial Text',
            rows = 25,
            allow_file_upload = zconf.ATDocument.allow_document_upload)
        ),

    TextField('studentName',
        required = False,
        searchable = True,
        storage = AnnotationStorage(migrate=True),
        widget = StringWidget(
            description = """The name of the student appears at the bottom of the testimonial""",
            label = 'Student Name',
            rows = 25,
            allow_file_upload = zconf.ATDocument.allow_document_upload)
        ),

    ImageField(
        name='testimionialImage',
        languageIndependent=True,
        storage=AnnotationStorage(),
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
        widget=ImageWidget(
            label='Testimonial Image',
            description="""The testimonial image associated with this testimonial.""",
            i18n_domain='oxford.testimonial',
            show_content_type = False,
        ),
    ),

))

TestimonialSchema['description'].widget.visible = False

finalizeATCTSchema(TestimonialSchema)
