<template>
  <div class="home-page">
    <h1 class="display-5 fw-bold text-center">
      Test App
    </h1>

    <div class="col-lg-6 mx-auto zones mb">
      <zone-editable
        v-for="zone in zones"
        :id="zone.id"
        :name="zone.name"
        :updated_at="zone.updated_at"
        :distributions="zone.distributions"
        :key="zone.uid"
        @edit="zone.name = $event.name"
        class="zone"
      />
    </div>
    <a class="fw-bold text-center btn btn-primary" href="/api/zones/create"> create a ToDO</a>
    <h1 class="display-5 fw-bold text-center">
      To Do List
    </h1>

    <ul class="col-lg-6 mx-auto">
      <li>Add the percentage symbol to each number</li>
      <li>Fix the cancel button</li>
      <li>Be able to edit each percentage</li>
      <li>Be able to add more percentages</li>
      <li>Be able to remove percentages</li>
      <li>When the user is not able to save due some error it must be showed</li>
      <li>The sum of all percentages must be ensured to be 100% in anyway</li>
      <li>The percentage must be integer</li>
      <li>The zone name cannot be empty</li>
      <li>The zone name cannot have more than one space between each word</li>
      <li>The zone name cannot have spaces at start or the end</li>
      <li>Show the updated_at field value near the each zone name</li>
      <li>Create a new field updated_at it only going to store the date when the name field change</li>
      <li>Add an animation while the element is being saved</li>
      <li>The zone name cannot be repeated in any way</li>
    </ul>
  </div>
</template>

<script>
import ZoneEditable from './ZoneEditable.vue';

export default {
  name: 'HomePage',
  components: {
    ZoneEditable
  },
  props: {
    context: {
      type: Object
    }
  },
  data() {
    return {
      zones: [],
      zoneUid: 0
    };
  },
  mounted() {
    this.zones = this.context.zones.map(data => {
      return {
        id: data.id,
        name: data.name,
        updated_at:data.updated_at,
        uid: this.zoneUid++,
        distributions: data.distributions
      };
    });
  }
}
</script>

<style type="text/scss" lang="scss">
@import 'resources/scss/variables.scss';

.home-page {
  .zones {
    display: flex;
    gap: 4px;
    flex-direction: column;
  }
}
</style>
