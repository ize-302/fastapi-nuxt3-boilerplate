<template>
  <div>
    <h1>Notes</h1>
    <p v-if="!notes.length && loading">Loading</p>
    <p v-if="notes.length && !loading">No notes to display</p>
    <ul v-else>
      <li v-for="(note, index) in notes" :key="note.id">
        {{ note.note }}
      </li>
    </ul>
  </div>
</template>

<script setup>
let notes = ref([]);
let loading = ref(true);

onMounted(async () => {
  await useFetch(`http://localhost:8000`)
    .then((response) => {
      notes.value = response.data.value;
    })
    .catch((err) => {
      console.log(err);
    });
});
</script>
