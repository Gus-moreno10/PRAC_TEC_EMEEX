from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    message = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        subject = request.form.get("subject", "").strip()
        contact_message = request.form.get("message", "").strip()

        if name and email and subject and contact_message:
            message = {
                "type": "success",
                "text": f"Gracias, {name}. Tu mensaje fue recibido correctamente.",
            }
        else:
            message = {
                "type": "danger",
                "text": "Por favor completa todos los campos del formulario.",
            }

    profile = {
        "name": "Sergio Moreno",
        "role": "Desarrollador Web y Estudiante Universitario",
        "summary": (
            "Me especializo en el desarrollo de sitios web modernos, funcionales y "
            "adaptables, con interés en backend con Python y diseño de interfaces."
        ),
        "email": "sergiomoreno@gmail.com",
        "phone": "73087120",
        "location": "El Alto, La Paz",
    }

    skills = [
        {"name": "Python", "level": 90},
        {"name": "Flask", "level": 88},
        {"name": "HTML5", "level": 95},
        {"name": "CSS3", "level": 90},
        {"name": "Bootstrap", "level": 85},
        {"name": "JavaScript", "level": 78},
    ]

    projects = [
        {
            "title": "Sistema de Gestión Académica",
            "description": (
                "Aplicación web para administrar estudiantes, cursos y calificaciones "
                "mediante una interfaz clara y organizada."
            ),
            "technologies": ["Python", "Flask", "SQLite", "Bootstrap"],
            "image": "img/project-1.svg",
        },
        {
            "title": "Tienda Virtual Responsive",
            "description": (
                "Diseño y desarrollo de una tienda en línea adaptable a móviles, con "
                "catálogo de productos y carrito visual."
            ),
            "technologies": ["HTML", "CSS", "Bootstrap", "Jinja2"],
            "image": "img/project-2.svg",
        },
        {
            "title": "Panel de Portafolio Profesional",
            "description": (
                "Sitio personal para mostrar experiencia, proyectos y medios de contacto "
                "con enfoque moderno y presentación atractiva."
            ),
            "technologies": ["Flask", "Jinja2", "CSS", "UI Design"],
            "image": "img/project-3.svg",
        },
    ]

    return render_template(
        "index.html",
        profile=profile,
        skills=skills,
        projects=projects,
        message=message,
    )


if __name__ == "__main__":
    app.run(debug=True)
