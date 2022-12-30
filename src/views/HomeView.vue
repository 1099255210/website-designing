<script setup>
import Welcome from '../components/Welcome.vue'
</script>

<template>
  <v-row>
    <v-col cols="3">
      <v-card class="mx-auto" max-width="344" variant="outlined">
        <v-card-item>
          <div class="text-overline mb-1">Welcome</div>
          <div class="text-h6 mb-1">欢迎</div>
        </v-card-item>
      </v-card>
    </v-col>
    <v-col cols="4">
      <Welcome />
    </v-col>
    <v-col cols="5">
      <v-card class="mx-auto" max-width="600">
        
      </v-card>
    </v-col>
  </v-row>
</template>