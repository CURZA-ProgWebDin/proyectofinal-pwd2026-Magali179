<template>
    <div>

        <header class="barra-superior">

            <h1 class="titulo-app">Librería Suipacha</h1>

            <nav class="menu-superior">

                <div v-if="!authStore.is_authenticated" class="opcion-menu">
                    <img src="@/assets/icons/libro.svg" alt="Libros">
                    <span>Libros</span>
                </div>

                <RouterLink v-else to="/libros" class="opcion-menu">
                    <img src="@/assets/icons/libro.svg" alt="Libros">
                    <span>Libros</span>
                </RouterLink>

                <div v-if="!authStore.is_authenticated" class="opcion-menu">
                    <img src="@/assets/icons/usuario.svg" alt="Usuarios">
                    <span>Usuarios</span>
                </div>

                <RouterLink v-else to="/usuarios" class="opcion-menu">
                    <img src="@/assets/icons/usuario.svg" alt="Usuarios">
                    <span>Usuarios</span>
                </RouterLink>

                <div class="opcion-menu">
                    <img src="@/assets/icons/ventas.svg" alt="Ventas">
                    <span>Ventas</span>
                </div>

                <div class="opcion-menu">
                    <img src="@/assets/icons/movimientos.svg" alt="Movimientos">
                    <span>Movimientos</span>
                </div>

            </nav>

        </header>

        <RouterView />

    </div>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth'//traemos store de autenticacion

const authStore = useAuthStore() //instancia del store para poder consultar, decidir si libro esta bloqueado o habilitado
</script>

<style scoped>

.barra-superior {
    height: 75px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 35px;
    background-color: #F6D3A7;
}

.titulo-app {
    margin: 0;
    font-size: 28px;
    color: #392714;
}

.menu-superior {
    display: flex;
    align-items: center;
    gap: 25px;
}

.opcion-menu {
    display: flex;
    align-items: center;
    gap: 8px;
    color: #392714;
    font-size: 16px;
    font-weight: 500;
}

.opcion-menu img {
    width: 28px;
    height: 28px;
}

</style>
