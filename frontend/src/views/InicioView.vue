<template>
    <div class="inicio-page">
        <h1>Inicio</h1>

        <p>Bienvenido a Librería Suipacha</p>
    </div>
</template>

<script setup>

</script>

<style scoped>
.inicio-page {  /*espacio interno al contenido para que no quede pegado a los bordes.*/
    padding: 30px;
}

.inicio-page h1 {
    margin-bottom: 10px; /*separamos el título del texto que viene debajo.*/
}

.inicio-page p { /*eliminamos el margen que el navegador coloca automáticamente en el párrafo.*/
    margin: 0;
}
</style>
