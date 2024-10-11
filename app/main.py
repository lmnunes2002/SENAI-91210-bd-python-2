from services.usuario_services import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.connection import Session

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    service.criar_usuario("Renan", "Renan@email.com", "789")

    print("\nListando todos os usuários.")
    usuarios = service.listar_todos_usuarios()

    for usuario in usuarios:
        print(f"{usuario.id} - {usuario.email}")

if __name__ == "__main__":
    main()