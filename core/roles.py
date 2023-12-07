from rolepermissions.roles import AbstractUserRole


class Administrador(AbstractUserRole):
    available_permissions = {'ver_ofertas': True, 'editar_ofertas': True,           'remover_ofertas': True, 'adicionar_ofertas': True, 'ver_candidatos': True, 'excluir_candidatos': True, 'ver_contatos': True, 'excluir_contatos': True}


class Usuario(AbstractUserRole):
    available_permissions = {'ver_ofertas': True, 'enviar_curriculo': True,             'enviar_contato': True}
