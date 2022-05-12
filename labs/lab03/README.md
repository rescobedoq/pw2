<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE INGENIERÍA DE SISTEMAS E INFORMÁTICA</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
        </tr>
    </theader>
    <tbody>
        <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio</td></tr>
        <tr><td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td><td><span style="font-weight:bold;">Código</span>: GUIA-PRLD-001</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">GUÍA DE LABORATORIO</span><br />
</div>


<table>
<theader>
<tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
<tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 2</td></tr>
<tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Ajax y NodeJS</td></tr>
<tr>
<td>NÚMERO DE PRÁCTICA:</td><td>03</td><td>AÑO LECTIVO:</td><td>2022 A</td><td>NRO. SEMESTRE:</td><td>III</td>
</tr>
<tr>
<td>FECHA INICIO::</td><td>09-May-2022</td><td>FECHA FIN:</td><td>13-May-2022</td><td>DURACIÓN:</td><td>04 horas</td>
</tr>
<tr><td colspan="6">RECURSOS:
    <ul>
        <li>https://www.w3schools.com/nodejs/nodejs_intro.asp</li>
        <li>https://nodejs.org/en/docs/guides/getting-started-guide/</li>
        <li>https://nodejs.dev/learn</li>
        <li>https://www.w3schools.com/js/js_api_fetch.asp</li>
        <li>https://expressjs.com/es/</li>
        <li>https://developer.mozilla.org/es/docs/Web/API/Fetch_API/Using_Fetch</li>
        <li>https://developer.mozilla.org/es/docs/Learn/Server-side/Express_Nodejs/Introduction</li>
    </ul>
</td>
</<tr>
<tr><td colspan="6">DOCENTES:
<ul>
<li>Richart Smith Escobedo Quispe - rescobedoq@unsa.edu.pe</li>
</ul>
</td>
</<tr>
</tdbody>
</table>

# Ajax y NodeJS

[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]

[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]

#

## OBJETIVOS TEMAS Y COMPETENCIAS

### OBJETIVOS

-   Aprender peticiones asíncronas en JavaScript usando JSON para la comunicación.
-   Programar en BackEnd usando JavaScript.
-   Entender el concepto de promises y los objetos no bloqueantes

### TEMAS
- Objetos asíncronos
- Comunicación con POST y GET
- Programación en el backend 

<details>
<summary>COMPETENCIAS</summary>

- C.c Diseña responsablemente sistemas, componentes o procesos para satisfacer necesidades dentro de restricciones realistas: económicas, medio ambientales, sociales, políticas, éticas, de salud, de seguridad, manufacturación y sostenibilidad.
- C.m Construye responsablemente soluciones siguiendo un proceso adecuado llevando a cabo las pruebas ajustada a los recursos disponibles del cliente.
- C.p Aplica de forma flexible técnicas, métodos, principios, normas, estándares y herramientas de ingeniería necesarias para la construcción de software e implementación de sistemas de información.

</details>

## CONTENIDO DE LA GUÍA

### MARCO CONCEPTUAL

-   https://www.w3schools.com/nodejs/nodejs_intro.asp
-   https://nodejs.org/en/docs/guides/getting-started-guide/
-   https://nodejs.dev/learn
-   https://www.w3schools.com/js/js_api_fetch.asp
-   https://expressjs.com/es/
-   https://developer.mozilla.org/es/docs/Web/API/Fetch_API/Using_Fetch
-   https://developer.mozilla.org/es/docs/Learn/Server-side/Express_Nodejs/Introduction

-   Instale NodeJS
-   Cree un nuevo proyecto NodeJS.
-   Cree un archivo index.js
    ```sh
    const http = require('http');
    const server = http.createServer((request, response) => {
        console.log(request.url);
        response.end("Hola mundo");
    });
    server.listen(3000);
    console.log("Escuchando en: http://localhost:3000")
    ```
-   Luego lance el servidor con:    
    ```sh
    node index.js
    ```
-   Note que console imprime en la salida estándar y el cliente sólo recibe el texto “Hola Mundo”. http://127.0.0.1:3000/

-   El siguiente código modifica algunas líneas para usar un framework llamado express y  devolver un archivo index.html
-   Para usar este código debe instalar express con npm: 
    ```sh
    $ npm install express    
    ```
    ```sh
    const path = require('path');
    const express = require('express');
    const app = express();

    app.listen(3000, () => {
        console.log("Escuchando en: http://localhost:3000")

    });

    app.get('/', (request, response) => {
        response.sendFile(path.resolve(__dirname, 'index.html'));
    });
    ```
-   Deberá crear un archivo index.html en el directorio de su proyecto.
-   Note que el servidor espera recibir una petición de tipo GET y el URL no contiene el nombre del archivo.

## EJERCICIO RESUELTO POR EL DOCENTE

-   Cree una aplicación web que ejecute javascript en el cliente (dentro de la carpeta pub) y nodejs en el servidor.
    ```sh
    const path = require('path');
    const express = require('express');
    const app = express();
    app.use(express.static('pub'));
    app.listen(3000, () => {
        console.log("Escuchando en: http://localhost:3000")

    });

    app.get('/', (request, response) => {
        response.sendFile(path.resolve(__dirname, 'index.html'));
    });
    ```
-   Cree una aplicación web que realice una petición ajax en el lado del cliente y responda usando nodejs en el lado del servidor.
-   En el lado del servidor :
    ```sh
    const fs = require('fs')
    const path = require('path')
    const express = require('express')
    const app = express()
    app.use(express.static('pub'))

    app.listen(3000, () => {
        console.log("Escuchando en: http://localhost:3000")
    });

    app.get('/', (request, response) => {
        response.sendFile(path.resolve(__dirname, 'index.html'))
    })

    app.get('/recitar', (request, response) => {
        fs.readFile(path.resolve(__dirname, 'priv/poema.txt'), 'utf8',
            (err, data) => {
                if (err) {
                    console.error(err)
                    response.status(500).json({
                        error: 'message'
                    })
                    return
                }
                response.json({
                    text: data.replace(/\n/g, '<br>')
                })
            })
        //
    })
    ```

-   En el lado del cliente:
    ```sh
    function recitar() {
        const url = 'http://localhost:3000/recitar'
        fetch(url).then(
            response => response.json()
        ).then(
            data => {
                document.querySelector("#poema").innerHTML = data.text
            }
        )
    }
    ```
-   Si tiene errores lea: https://medium.com/zero-equals-false/using-cors-in-express-cac7e29b005b

-   Cree una aplicación que haga peticiones AJAX usando POST a un servidor NodeJS
-   En el lado del servidor
    ```sh
    const fs = require('fs')
    const path = require('path')
    const express = require('express')
    const bp = require('body-parser')
    const MarkdownIt = require('markdown-it'),
        md = new MarkdownIt();
    const app = express()

    app.use(express.static('pub'))
    app.use(bp.json())
    app.use(bp.urlencoded({
        extended: true
    }))

    app.listen(3000, () => {
        console.log("Escuchando en: http://localhost:3000")
    })

    app.get('/', (request, response) => {
        response.sendFile(path.resolve(__dirname, 'index.html'))
    })

    app.post('/', (request, response) => {
        console.log(request.body)
        let markDownText = request.body.text
        console.log(markDownText)
        let htmlText = md.render(markDownText)
        response.setHeader('Content-Type', 'application/json')
        response.end(JSON.stringify({
            text: htmlText
        }))
    })
    ```
-   Note que tanto el tanto GET como POST comparten el mismo URL.

-   En el lado del cliente
    ```sh
    function recitar(markupText) {
	const url = 'http://localhost:3000/'
	const data = {
		text: markupText
	}
    console.log(data)
	const request = {
		method: 'POST', // Podría ser GET
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(data),
	}
	http = fetch(url, request)
	http.then(
		response => response.json()
	).then(
		data => {
			document.querySelector("#htmlCode").innerHTML = data.text
		}
        )
    }
    document.addEventListener('DOMContentLoaded', function () {
        const text = document.querySelector('#markupText')
        document.querySelector('#markupForm').onsubmit = () => {
            recitar(text.value)
            return false;
        }
    })
    ```

#

## EJERCICIOS PROPUESTOS
-   En grupos de 3 a 5 personas implemente una aplicación web que navegue sobre archivos Markdown y permita:
    1. Listas los archivos Markdown disponibles
    2. Ver el contenido de un archivo Markdown traducido a HTML
    3. Crear nuevos archivos MarkDown y almacenarlos en el servidor

-   La comunicación entre el cliente y el servidor tiene que ser usando JSON sólamente.
El cliente debe usar AJAX para sus peticiones
El servidor debe usar NodeJS
Su aplicación debe ser de página única, es decir que sólo habrá un archivo index.html y nada más.

-   Si los enlaces proporcionado en esta guía no le son suficientes, puede revisar códigos en Internet que le ayuden con cosas como ejemplos: listar un directorio en NodeJS; pero deberá incluir los enlaces correspondientes en sus archivos como comentarios y sólo podrá usar código de stackoverflow, incluir código de cualquier otra fuente está prohibido y se considerará actitud deshonesta.

#

## CUESTIONARIO
- En el Ejemplo "Hola Mundo" con NodeJS. ¿Qué pasó con la línea: "Content type ….."?
- En los ejercicios. ¿En qué lugar debería estar el archivo poema.txt?
- ¿Entiende la expresión regular en el código y se da cuenta de para qué es útil?
- Note que la respuesta del servidor está en formato JSON, ¿Habrá alguna forma de verla directamente?

#

## REFERENCIAS
-   JavaScript code using the latest ECMAScript. Packt Publishing Ltd, 2018.
-   Greg Lim. Beginning Node.js, Express & MongoDB Development. Amazon, 2019.
-   https://www.w3schools.com/nodejs/nodejs_intro.asp
-   https://nodejs.org/en/docs/guides/getting-started-guide/
-   https://nodejs.dev/learn
-   https://www.w3schools.com/js/js_api_fetch.asp
-   https://expressjs.com/es/
-   https://developer.mozilla.org/es/docs/Web/API/Fetch_API/Using_Fetch
-   https://developer.mozilla.org/es/docs/Learn/Server-side/Express_Nodejs/Introduction

#

[license]: https://img.shields.io/github/license/rescobedoq/pw2?label=rescobedoq
[license-file]: https://github.com/rescobedoq/pw2/blob/main/LICENSE

[downloads]: https://img.shields.io/github/downloads/rescobedoq/pw2/total?label=Downloads
[releases]: https://github.com/rescobedoq/pw2/releases/

[last-commit]: https://img.shields.io/github/last-commit/rescobedoq/pw2?label=Last%20Commit

[Debian]: https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white
[debian-site]: https://www.debian.org/index.es.html

[Git]: https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white
[git-site]: https://git-scm.com/

[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[github-site]: https://github.com/

[Vim]: https://img.shields.io/badge/VIM-%2311AB00.svg?style=for-the-badge&logo=vim&logoColor=white
[vim-site]: https://www.vim.org/

[Java]: https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white
[java-site]: https://docs.oracle.com/javase/tutorial/


[![Debian][Debian]][debian-site]
[![Git][Git]][git-site]
[![GitHub][GitHub]][github-site]
[![Vim][Vim]][vim-site]
[![Java][Java]][java-site]


[![License][license]][license-file]
[![Downloads][downloads]][releases]
[![Last Commit][last-commit]][releases]
