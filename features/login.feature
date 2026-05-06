Feature: Login Demoblaze

  Scenario: Login inválido con credenciales incorrectas
    Given que el navegador está listo
    When navego a "https://www.demoblaze.com"
    And hago clic en el botón de login
    And ingreso el usuario "usuario_invalido"
    And ingreso la contraseña "password_invalida"
    And confirmo el login
    Then debería ver un mensaje de error

  Scenario: Login válido exitosamente
    Given que el navegador está listo
    When navego a "https://www.demoblaze.com"
    And hago clic en el botón de login
    And ingreso el usuario "demoblaze"
    And ingreso la contraseña "demoblaze"
    And confirmo el login
    Then debería iniciar sesión exitosamente
