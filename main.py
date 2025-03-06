from mkdocs_macros.context import fix_url
from textwrap import dedent
from markdown2 import markdown
from markupsafe import Markup


def define_env(env):
    @env.macro
    def image(url: str, alt: str = "", class_name: str = "") -> str:
        url = fix_url(url)
        return f'<img src="{url}" alt="{alt}" class="{class_name}">'

    @env.macro
    def internal_link(url: str, text: str, class_name: str = "") -> str:
        url = env.conf["site_url"] + url + ".html"
        return f'<a href="{url}" class="{class_name}">{text}</a>'

    @env.macro
    def text_media_layout(
        content_md,
        media_path,
        media_alt="",
        media_type="image",
        media_position="right",
    ):
        if media_type == "video":
            media_html = dedent(
                f"""
                <div>
                    <iframe src="{media_path}" title="{media_alt}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                </div>
                """
            )
        else:
            media_html = dedent(
                f"""<div class="text-media__image" style="background-image: url({fix_url(media_path)});" aria-label="{media_alt}"/>"""
            )

        content_md = markdown(content_md)
        html = dedent(
            f"""<div class="text-media text-media-{media_position}">
                        <div class="text-media__content">
                            {content_md}
                        </div> 
                            {media_html}
                    </div>"""
        )
        return Markup(html)

    env.variables.stats_items = [
        {"icon": "valve", "value": "7", "label": "Sistemas de agua"},
        {"icon": "communities", "value": "33", "label": "Comunidades"},
        {"icon": "account_circle", "value": "2.400", "label": "Socios y usuarios/as"},
        {"icon": "groups", "value": "6.500", "label": "Población beneficiaria"},
        {"icon": "download", "value": "XX", "label": "Descargas"},
    ]

    env.variables.testimonials_data = [
        {
            "img_url": "assets/images/Foto_3_b.jpeg",
            "name": "Diana",
            "title": "Secretaria del Sistema ARA-Cangrejera",
            "content": "Desde que usamos la aplicación de AIGAR, los socios del sistema han tomado mayor conciencia sobre el uso del agua y ahora pueden pagar fácilmente a través del banco. Gracias a esto, hemos logrado reducir significativamente la deuda y mejorar la administración del servicio.",
        },
        {
            "img_url": "assets/images/Foto_4_a.jpg",
            "name": "Nancy",
            "title": "Secretaria del sistema JASACT",
            "content": "La aplicación ha sido de gran ayuda para nuestro sistema de agua. Nos permite llevar un mejor control de los socios y generar los recibos en mucho menos tiempo. Antes, tardaba hasta dos días en realizarlos manualmente, pero ahora con AIGAR solo 30 minutos. Esto me da más tiempo para dedicarme a otras tareas dentro del sistema.",
        },
    ]

    env.variables.partners_data = [
        {
            "logo_url": "assets/images/logos/acua.png",
            "name": "ACUA",
        },
        {
            "logo_url": "assets/images/logos/asaps.png",
            "name": "ASAPS",
        },
        {"logo_url": "assets/images/logos/icarto.png", "name": "iCarto"},
        {
            "logo_url": "assets/images/logos/isf.jpg",
            "name": "Ingeniería Sin Fronteras",
        },
    ]

    env.variables.funders_data = [
        {
            "logo_url": "assets/images/logos/xunta.png",
            "name": "Cooperación Galega",
        },
        {"logo_url": "assets/images/logos/aecid.png", "name": "AECID"},
    ]

    env.variables.contacts_data = [
        {
            "name": "ACUA",
            "email": "email@email.com",
            "phone": "+503 2314 0636",
            "location": "Barrio la Cruz, Avenida Monseñor Romero #31. </br> Zaragoza, La Libertad, El Salvador",
            "url": "https://www.acua.org.sv/",
            "logo_url": "assets/images/logos/acua.png",
        },
        {
            "name": "ASAPS",
            "email": "email@email.com",
            "phone": "+34 123 456 789",
            "location": "San Salvador, El Salvador",
            "url": "https://www.acua.org.sv/",
            "logo_url": "assets/images/logos/asaps.jpg",
        },
        {
            "name": "iCarto",
            "email": "info@icarto.es",
            "phone": "+34 881 927 808",
            "location": "C/ Rafael Alberti, 13 – 1ºD. </br>15008 A Coruña, España",
            "url": "https://icarto.es",
            "logo_url": "assets/images/logos/icarto.png",
        },
    ]
