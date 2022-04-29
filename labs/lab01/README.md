<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
        </tr>
    </theader>
    <tbody>
        <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio / Talleres / Centros de Simulación</td></tr>
        <tr><td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td><td><span style="font-weight:bold;">Código</span>: GUIA-PRLD-001</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">GUÍA DE LABORATORIO</span><br />
<span>(formato docente)</span>
</div>


<table>
<theader>
<tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
<tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 2</td></tr>
<tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Git - GitHub</td></tr>
<tr>
<td>NÚMERO DE PRÁCTICA:</td><td>01</td><td>AÑO LECTIVO:</td><td>2022 A</td><td>NRO. SEMESTRE:</td><td>III</td>
</tr>
<tr>
<td>FECHA INICIO::</td><td>25-Abr-2022</td><td>FECHA FIN:</td><td>29-Abr-2022</td><td>DURACIÓN:</td><td>04 horas</td>
</tr>
<tr><td colspan="6">RECURSOS A UTILIZAR:
<ul>
<li><a href="https://guides.github.com/">https://guides.github.com/</a></li>
<li><a href="https://git-scm.com/book/es/v2">https://git-scm.com/book/es/v2</a></li>
</ul>
</td>
</<tr>
<tr><td colspan="6">DOCENTES:
<ul>
<li>Richart Smith Escobedo Quispe (rescobedoq@unsa.edu.pe)</li>
</ul>
</td>
</<tr>
</tdbody>
</table>


# OBJETIVOS TEMAS Y COMPETENCIAS

## OBJETIVOS

- Aprender a manejar un sistema de control de versiones de manera colaborativa con varios
usuarios

## TEMAS
- Git
- GitHub

## COMPETENCIAS
- C.c Diseña responsablemente sistemas, componentes o procesos para satisfacer necesidades dentro de restricciones realistas: económicas, medio ambientales, sociales, políticas, éticas, de salud, de seguridad, manufacturación y sostenibilidad.
- C.m Construye responsablemente soluciones siguiendo un proceso adecuado llevando a cabo las pruebas ajustada a los recursos disponibles del cliente.
- C.p Aplica de forma flexible técnicas, métodos, principios, normas, estándares y herramientas de ingeniería necesarias para la construcción de software e implementación de sistemas de información.

# CONTENIDO DE LA GUÍA

## MARCO CONCEPTUAL
- git init
    - Crea un nuevo proyecto local, se crean archivos en el directorio oculto .git
    ```sh
    git init
    ```

- git config
    - Establece variables de configuración. Por ejemplo para los commits se necesita los datos del desarrollador. Se puede especificar el editor y hasta el tiempo que deseas almacenar tus credenciales en la cache y otras cosas más
    ```sh
    git config --global user.name "Richart Smith Escobedo Quispe"
    git config --global user.email rescobedoq@unsa.edu.pe
    git config --list
    git config user.name
    git config --global core.editor "code --wait"
    git config --global credential.helper 'cache --timeout=3600'
    ```

- git status
    - Permite verificar el estado de los archivos
    ```sh
    git status
    ```
- git add
    - Añade archivos al staging area. El punto "." agrega todos
    ```sh
    git add HolaMundo.java
    git .
    ```

- git commit
    - Sube los archivos al área de staging, en la máquina local. La opción -m permite escribir el mensaje en línea
    ```sh
    git commit -m "Probando el Hola Mundo"    
    ```

- git push
    - Permite subir archivos al repositorio remoto

- git show
    - Muestra detalles del commit actual
    ```sh
    git show
    ```

-   git log
    - Permite ver un resumen de los commit realizados
    ```sh
    git log
    git log --pretty=oneline
    git log --graph --pretty=oneline --abbrev-commit --all
    git log --pretty=format:"%h - %an, %ar : %s"
    git log -p -2
    ```

- git diff
    - Permite comparar los cambios en los archivos
    ```sh
    git diff
    ```

- git clone
    - Clona un repositorio remoto desde CERO
    ```sh
    git clone https://github.com/rescobedoq/pweb2.git
    ```

- git checkout
    - Permite regresar a versiones anteriores o saltar a otra rama
    ```sh
    git checkout master
    ```

- git pull
    - Permite descargar los cambios del repositorio remoto al directorio local

- git branch
    - Permite ver las ramas existentes o crea una rama alternativa al proyecto principal git branch -a

## EJERCICIO/PROBLEMA RESUELTO POR EL DOCENTE
Primer repositorio en GitHub
- Creamos un nuevo proyecto en GitHub
    - ![Nuevo Proyecto GitHub](github_proyecto_programacion.png)

- Crearemos un repositorio local usando git init
    ```sh
    pwd
    /home/richart/unsa/proyecto
    git init
    ```

- Crearemos un archivo Readme.md con contenido Markup
    ```sh
    echo "# Mi proyecto Git" > README.md
    ```

- Agregaremos este archivo al staging area usando git add .
    ```sh
    git status
    ```
    <pre>
    En la rama main

    No hay commits todavía

    Archivos sin seguimiento:
    (usa "git add <archivo>..." para incluirlo a lo que se será confirmado)
	README.md
    no hay nada agregado al commit pero hay archivos sin seguimiento presentes (usa "git add" para hacerles seguimiento)
    </pre>
    ```sh
    git add README.md
    ```

- Hacemos un primer commit en nuestro repositorio local 
    ```sh
    git commit -m "Mi primer proyecto en github"
    ```
- Asociamos el repositorio local con el repositorio remoto 
    ```sh
    git remote add origin https://github.com/rescobedoq/proyecto
    ```

- Actualizamos el repositorio remoto
    ```sh
    git push -u origin main
    ```

- Ahora podemos verificar en GitHub que nuestro repositorio se actualizó con el proyecto local
    - ![Readme.md](Readme.md.png)

- Cree una clase Java HolaMundo.java que imprima un saludo, compílelo, ignore archivos binarios, agregue archivo al stating area, haga commit y súbalo al repositorio GitHub.
    ```sh
    vim HolaMundo.java
    ```
    <pre>
    public class HolaMundo
    {
        public static void main(String args[]) {
        
            /** */
            System.out.println ("¡Hola mundo!");

        }
    }
    </pre>
    ```sh    
    java -version
    ```
    <pre>
    openjdk version "11.0.14" 2022-01-18
    </pre>
    ```sh
    javac HolaMundo.java
    java HolaMundo
    ```
    <pre>
    ¡Hola mundo!
    </pre>
    ```sh
    vim .gitignore
    ```
    <pre>
    *.class
    .gitignore
    </pre>
    ```sh
    git add HolaMundo.java
    git commit -m "Hola Mundo"
    git push -u origin main
    ```
    
## EJERCICIOS/PROBLEMAS PROPUESTOS
- Cree una cuenta de usuario en github.
- Configure su cuenta de estudiante (https://education.github.com/pack).
- Cree un nuevo proyecto personal y desarrolle el ejercicio resuelto en clase. Haga 3 commits y muestre los 3 últimos.
- Cree un proyecto grupal para resolver el siguiente problema: Se desea crear una clase Calculator en Java, que tenga las siguientes operaciones: add, sub, mul, div, mod; estas operaciones recibirán dos enteros y devolverán un entero. (Forme grupos de 3 a 5 personas). Cree ramas para cada integrante y cada cierto tiempo una las ramas al main.

## CUESTIONARIO
- ¿Por qué Git es una herramienta importante en el curso de Programación Web 2?

## REFERENCIAS Y BIBLIOGRÁFIA RECOMENDADAS
- https://guides.github.com/
- https://git-scm.com/book/es/v2




