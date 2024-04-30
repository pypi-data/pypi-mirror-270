Feature: Demo Web Aplicacion OpenCart

  @Prueba1 @REG
  Scenario Outline: Registro Exitoso
    Given Usuario ingresa a la web de OpenCart "<url>"
    And Usuario da click en la opción Registro
    And Usuario llena los datos de Registro con "<nombre>", "<apellido>", "<correo>" y "<telefono>"
    And Usuario ingresa sus claves
    Then Se verifica el registro correcto

    Examples:
      | url                            | nombre | apellido | correo                 | telefono  |
      | https://opencart.abstracta.us/ | Juan   | Perez    | nuevo1xx1@example.com  | 958025002 |
      | https://opencart.abstracta.us/ | Maria  | Lopez    | nuevo1xx12@example.com | 999999999 |

  @Prueba2 @REG
  Scenario Outline: Login Exitoso
    Given Usuario ingresa nuevamente a la web de OpenCart "<url>"
    When Usuario da click en la opcion Login
    And Usuario ingesa su correo "<correo>"
    And Usuario ingresa su contraseña
    Then Se verifica el Login correcto

    Examples:
      | url                            | nombre | apellido | correo               | telefono  |
      | https://opencart.abstracta.us/ | Juan   | Perez    | nuevo11@example.com  | 958025002 |
      | https://opencart.abstracta.us/ | Maria  | Lopez    | nuevo112@example.com | 999999999 |
