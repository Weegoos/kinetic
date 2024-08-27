<template>
  <div class="">
    <div class="row q-gutter-sm">
      <div class="col">
        <p class="text-bold headline">Мои результаты</p>
        <span class="greetingText">Добро пожаловать Анна Смагулова</span>
      </div>
      <div class="col q-mr-sm" align="right">
        <q-card class="filter row" align="left">
          <div class="col">
            <img src="../../assets/result/Icon.png" alt="" />
          </div>
          <div class="col-9" align="left">
            <q-input
              dense
              v-model="text"
              type="text"
              label="Фильтрация"
              list="dateList"
            />
            <datalist id="dateList">
              <div v-for="(items, id) in dates" :key="id">
                <option :value="items.date"></option>
              </div>
            </datalist>
          </div>
        </q-card>
      </div>
    </div>
  </div>
</template>

<script setup>
const dates = [
  {
    date: "12-07-2024",
  },
  {
    date: "12-07-2023",
  },
];
</script>

<style scoped>
.headline {
  font-size: 24px;
  color: #464255;
}

.greetingText {
  font-size: 16px;
  color: #a3a3a3;
}

.filter {
  max-width: 250px;
}

.filter img {
  background: linear-gradient(#2d9cdb 15%);
  color: white;
}
</style>
