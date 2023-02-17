<!-- <template>
  <v-row>
    <v-col cols="3">
      <v-card class="mx-auto" max-width="344" variant="outlined">
        <v-card-item>
          <div class="text-overline mb-1">My favourite</div>
          <div class="text-h6 mb-1">我的收藏</div>
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
</template> -->

<template>
  <v-app>
    <div class="d-flex justify-center ma-4">
      <v-btn color="primary" @click="alert = !alert"> Toggle </v-btn>
    </div>
    <div class="d-flex justify-center ma-4">
      <v-col sm="6">
        <v-alert
          color="indigo"
          dark
          transition="scale-transition"
          v-model="alert"
        >
          Shaped alert
        </v-alert>
      </v-col>
    </div>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data: () => ({
    alert: false,
  }),
};
</script>