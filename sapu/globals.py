#coding:utf-8

################################################################################
#
# Errors
#
################################################################################

ERROR__INVALID_FORM = u"Los datos son inválidos"
ERROR__INVALID_USER_OR_PASSWORD = u"Usuario o contraseña incorrectos."
ERROR__NO_POST_DATA = u"No se encontraron datos que procesar"
ERROR__USER_NOT_ACTIVE = u"El usuario no está activado."
ERROR__FORBIDDEN = u"No cuentas con los permisos necesarios"
ERROR__SERVER_ERROR = u"Error en el servidor. Intente de nuevo más tarde."
ERROR__DUPLICATE = u"Ya existe un ítem con el mismo nombre"
ERROR__INVALID_UPLOAD = u"Error al subir el archivo"


################################################################################
#
# Messages
#
################################################################################

MESSAGE__CREATION_SUCCESS_M = u"{model_name} {item_name} creado"
MESSAGE__EDIT_SUCCESS_M = u"{model_name} {item_name} modificado"

MESSAGE__CREATION_SUCCESS_F = u"{model_name} {item_name} creada"
MESSAGE__EDIT_SUCCESS_F = u"{model_name} {item_name} modificada"


################################################################################
#
# Form Fields
#
################################################################################

FIELD__PASSWORD = u"Contraseña"
FIELD__USERNAME = u"Usuario"

FIELD__PROJECT = u"Proyecto"
FIELD__INSTITUTION = u"Institución"
FIELD__STAGE = u"Etapa"
FIELD__STATE = u"Estado"
FIELD__PROJECT_TYPE = u"Tipo de proyecto"
FIELD__COMMENT = u"Comentario"
FIELD__TASK = u"Tarea"
FIELD__PERMISSION = u"Permiso"

FIELD__EMPLOYEE = u"Empleado"
FIELD__SUPERVISOR = u"Supervisor"
FIELD__PROJECT_MANAGER = u"Jefe de proyecto"
FIELD__SYSTEM_ADMIN = u"Administrador del sistema"

FIELD__NAME = u"Nombre"
FIELD__TELEPHONE = u"Teléfono"
FIELD__ADDRESS = u"Dirección"
FIELD__EMAIL = u"Correo Electrónico"
FIELD__IS_CLIENT = u"¿Es Cliente?"
FIELD__CONTACT_POINT = u"Punto de Contacto"


################################################################################
#
# Form Prefixes
#
################################################################################

PREFIX__FORM_INSTITUTION = 'institution'
PREFIX__FORM_PROJECT_TYPE = 'project_type'
PREFIX__FORM_PROJECT = 'project'
PREFIX__FORM_STAGE = 'stage'
PREFIX__FORM_TASK = 'task'
PREFIX__FORM_COMMENT = 'comment'
PREFIX__FORM_EMPLOYEE = 'employee'
PREFIX__FORM_PERMISSION = 'permission'

################################################################################
#
# Templates
#
################################################################################

TEMPLATE__LOGIN = "sections/login.html"
TEMPLATE__INSTITUTIONS = "sections/institutions.html"
TEMPLATE__PROJECT_TYPES = "sections/project-types.html"
TEMPLATE__PROJECTS = "sections/projects.html"
TEMPLATE__STAGES = "sections/stages.html"
TEMPLATE__STAGE_DETAIL = "sections/stage-detail.html"
TEMPLATE__USERS = "sections/users.html"
TEMPLATE__MODAL = "components/modal_edit.html"


################################################################################
#
# Modals
#
################################################################################

MODAL_EDIT__INSTITUTION = "institution"
MODAL_EDIT__PROJECT = "project"
MODAL_EDIT__PROJECT_TYPE = "project_type"
MODAL_EDIT__STAGE = "stage"
MODAL_EDIT__COMMENT = "comment"
MODAL_EDIT__TASK = "task"
MODAL_EDIT__EMPLOYEE = "employee"
MODAL_EDIT__PERMISSION = "permission"

################################################################################
#
# Modal Actions
#
################################################################################

MODAL_ACTION__CREATE = u"Crear"
MODAL_ACTION__EDIT = u"Editar"
MODAL_ACTION__DELETE = u"Eliminar"
MODAL_ACTION__CANCEL = u"Cancelar"

OPTION_NAME__MODAL_FORM_VIEW = "view"
OPTION_NAME__MODAL_FORM_ADD = "add"
OPTION_NAME__MODAL_FORM_EDIT = "edit"


################################################################################
#
# Model Names
#
################################################################################

MODEL_NAME__INSTITUTION = u"institución"
MODEL_NAME__PROJECT = u"proyecto"
MODEL_NAME__PROJECT_TYPE = u"tipo de proyecto"
MODEL_NAME__STAGE = u"etapa"
MODEL_NAME__COMMENT = u"comentario"
MODEL_NAME__TASK = u"tarea"
MODEL_NAME__EMPLOYEE = u"usuario"
MODEL_NAME__PERMISSION = u"permiso"


################################################################################
#
# Classes
#
################################################################################


class Modal:

    def __init__(
            self,
            name=u"",
            action=None,
            main_forms=None,
            accept_button_text=MODAL_ACTION__CREATE,
            accept_button_link=u"#",
            cancel_button_text=MODAL_ACTION__CANCEL,
            cancel_button_link=u"#"
    ):
        self.name = name
        self.action = action
        self.main_forms = main_forms
        self.accept_button_text = accept_button_text
        self.accept_button_link = accept_button_link
        self.cancel_button_text = cancel_button_text
        self.cancel_button_link = cancel_button_link


class ModalForm:

    def __init__(
            self,
            title=u"",
            description=u"",
            form=None,
            buttons=None
    ):
        self.title = title
        self.description = description
        self.form = form
        self.buttons = buttons