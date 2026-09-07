<template>
    <div class="libro-page">

        <h1>Libros</h1>

        <p>Gestión de libros de Librería Suipacha</p>
        <button class="btn-libro">Agregar libro</button>

        <div class="libros-lista">

            <h2>Listado de libros</h2>

            <table>
                <thead>
                    <tr>
                        <th>Título</th>
                        <th>Autor</th>
                        <th>Precio</th>
                        <th>Stock</th>
                    </tr>
                </thead>

                <tbody>
                    <tr>
                        <td>Ejemplo de libro</td>
                        <td>Autor de ejemplo</td>
                        <td>$10000</td>
                        <td>10</td>
                    </tr>
                </tbody>
            </table>

        </div>

    </div>
</template>

<script setup>

</script>

<style scoped>

.libro-page {
    padding: 30px;
}

.libro-page h1 {
    margin-bottom: 10px;
}

.libro-page p {
    margin-bottom: 20px;
}

.btn-libro {
    padding: 10px 15px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
}

.libros-lista {
    margin-top: 30px;
}

.libros-lista h2 {
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