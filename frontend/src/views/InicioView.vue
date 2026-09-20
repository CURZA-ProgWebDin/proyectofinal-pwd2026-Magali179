<template>
    <div class="inicio-page">

        <div class="inicio-contenido">

            <div class="mensaje-bienvenida">
                Bienvenido al sistema de gestión
            </div>

        </div>

    </div>
</template>

<script setup>

</script>

<style scoped>

.mensaje-bienvenida {
    display: inline-block;
    padding: 20px 40px;
    background-color: rgba(255, 250, 243, 0.90);
    border: 2px solid #392714;
    border-radius: 10px;
    color: #392714;
    font-size: 28px;
    font-weight: 500;
}
.inicio-page {
    min-height: 100vh;
    padding: 40px;
    background-image: 
        linear-gradient(rgba(255, 248, 238, 0.65), rgba(255, 248, 238, 0.65)),
        url('@/assets/images/fondo-libreria.png');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.inicio-contenido {
    max-width: 900px;
    margin: 0 auto;
    text-align: center;
    padding-top: 120px;
}

.inicio-contenido h1 {
    color: #392714;
    font-family: sans-serif;
    font-size: 36px;
    margin-bottom: 10px;
}

.inicio-contenido p {
    color: #5a4030;
    margin-bottom: 30px;
}

.opciones {
    display: grid;
    grid-template-columns: repeat(2, 250px);
    gap: 18px;
    justify-content: center;
}

.opcion {
    background-color: rgba(255, 250, 243, 0.92);
    border: 2px solid #896449;
    border-radius: 15px;
    padding: 15px;
    height: 105px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 8px;
}

.opcion img {
    width: 80px;
    height: 80px;
}

.opcion span {
    color: #392714;
    font-size: 20px;
    font-weight: bold;
}
</style>