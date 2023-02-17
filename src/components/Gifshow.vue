<script setup>
  defineProps({
    link: {
      type: String
    }
  })
</script>

<template>
  <div class="contain">
    <img :src="link" alt="Image">
  </div>
</template>