<script setup>
import { RouterLink, RouterView } from "vue-router";

</script>

<template>
  <header>
    <div class="wrapper">
      <nav class="navbar navbar-expand navbar-dark bg-dark">
        <div class="container-fluid">
          <RouterLink to="/" class="navbar-brand">Instruções</RouterLink>
          <!-- <button
            class="navbar-toggler"
            type="button"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button> -->
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
           
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">

              <li class="nav-item">
                <RouterLink to="/operators" class="nav-link"
                  >Operadoras</RouterLink
                >
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped></style>
