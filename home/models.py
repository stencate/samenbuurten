from django.db import models

from wagtail.models import Page

from wagtail.fields import RichTextField

# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


# Create your models here.
class HomePage(Page):
    # add the Hero section of HomePage:
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )

    hero_text_one = models.CharField(
        blank=True,
        max_length=255,
        help_text="First hero slogan",
        verbose_name="Hero slogan 1",
    )
    hero_text_two = models.CharField(
        blank=True,
        max_length=255,
        help_text="Second hero slogan",
        verbose_name="Hero slogan 2",
    )

    hero_cta = models.CharField(
        blank=True,
        verbose_name="Hero CTA",
        max_length=255,
        help_text="Text to display on Call to Action",
    )
    hero_cta_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Hero CTA link",
        help_text="Choose a page to link to for the Call to Action",
    )

    body = RichTextField(blank=True)

    # modify your content_panels:
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("image"),
                FieldPanel("hero_text_one"),
                FieldPanel("hero_text_two"),
                FieldPanel("hero_cta"),
                FieldPanel("hero_cta_link"),
            ],
            heading="Hero section",
        ),
        FieldPanel("body"),
    ]
