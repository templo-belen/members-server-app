import enum

class MaritalStatusType(str, enum.Enum):
    soltero = "Soltero(a)"
    casado = "Casado(a)"
    viudo = "Viudo(a)"
    divorciado = "Divorciado(a)"
    union_libre = "Unión libre"
    separado = "Separado(a)"
    vuelto_a_casar = "Vuelto a casar"
    otro = "Otro"

class GenderType(str, enum.Enum):
    femenino = "Femenino"
    masculino = "Masculino"

class RoleType(str, enum.Enum):
    miembro = "Miembro"
    miembro_asamblea = "Miembro asamblea"
    inactivo = "Inactivo"
    visitante = "Visitante"

class CellLeadershipType(str, enum.Enum):
    nuevo_creyente = "Nuevo creyente"
    padre_espiritual = "Padre espiritual"
    lider_asociado = "Líder asociado"
    lider_celula = "Líder de célula"
    lider_seccional = "Líder seccional"
    obrero = "Obrero"
    pastor_zona = "Pastor de zona"
    pastor_principal = "Pastor principal"

class LeadershipType(str, enum.Enum):
    musico = "Músico"
    maestro_distrito_infantil = "Maestro distrito infantil (D.I.)"
    maestro_junior = "Maestro junior"
    maestro_180 = "Maestro 180 grados"
    maestro_universitario = "Maestro universitario"
    maestro_retbelen = "Maestro RetBelen"
    no_aplica = "N/A"

class HousingType(str, enum.Enum):
    propia = "Propia"
    familiar = "Familiar"
    alquiler = "Alquiler"

class LeavingReasonType(str, enum.Enum):
    cambio_iglesia = "Cambió de iglesia"
    cambio_residencia = "Cambió de residencia"
    personales = "Personales"
    enfermedad = "Enfermedad"
    muerte = "Muerte"
    cambio_creencia = "Cambió de creencia"
    otro = "Otro"

class BloodType(str, enum.Enum):
    a_positive = "A+"
    a_negative = "A-"
    b_positive = "B+"
    b_negative = "B-"
    ab_positive = "AB+"
    ab_negative = "AB-"
    o_positive = "O+"
    o_negative = "O-"
