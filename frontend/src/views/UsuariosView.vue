<template>
    <div class="usuarios-page"> <!--  es un contenedor.La class nos permite identificar este div desde CSS. -->

        <h1>Usuarios</h1>

        <p>Gestión de usuarios de Librería Suipacha</p>
       
        <div class="usuarios-lista">

            <h2>Listado de usuarios</h2>

            <table>
                <thead>
                    <tr>
                        <th>Usuario</th>
                        <th>Nombre</th>
                        <th>Rol</th>
                    </tr>
                </thead>

                <tbody>
                    <tr>
                        <td>usuario</td>
                        <td>Usuario de ejmplo</td>
                        <td>Operador</td>
                    </tr>
                </tbody>
            </table>

        </div>

    </div>
</template>

<script setup> /* vamos a colocar la lógica de la vista. */

</script>

<style>
.usuarios-page {
    padding: 30px;
}

.usuarios-page h1 {
    margin-bottom: 10px;
}

.usuarios-page p {
    margin-bottom: 20px;
}

.usuarios-lista {
    margin-top: 30px;
}

.usuarios-lista h2 {
    margin-bottom: 15px;
}

table {
    width: 100%;
    border-collapse: collapse;
}

th,
td {
    padding: 10px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
</style>