<template>
  <div class="zone-editable">
    <div
      v-if="display"
      class="zone-display"
    >
      <div>
        <strong>{{ name }}</strong><small>{{ updated_at }}</small> {{ distributionDisplay }}
      </div>

      <button
        class="btn btn-primary"
        @click="setDisplay(false)"
        :disabled="saving"
      >
        Edit
      </button>
    </div>
    <div
      v-else
      class="zone-edit"
    >
      <input
        v-model="form.name"
        placeholder="Zone name"
        class="form-control"
        :disabled="saving"
      >

      <div class="zone-edit-distributions">
        <div v-for="distribution in form.distributions">
          <input
            v-model="distribution.percentage"
            placeholder="Percentage"
            class="form-control"
          >
        </div>
      </div>

      <div class="zone-edit-actions">
        <button class="btn btn-secondary" @click="setDisplay(true)" :disabled="saving">
         Cancel
        </button>

        <button
          class="btn btn-success"
          @click="save"
          :disabled="saving"
        >
          Save
        </button>
        <button
          class="btn btn-danger"
          @click="delete_item"
          :disabled="saving"
        >
          Delete
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ZoneEditable',
  props: {
    name: String,
    updated_at: String,
    id: Number,
    distributions: Array,
  },
  data() {
    return {
      display: true,
      form: {
        name: '',
        updated_at: '',
        distributions: [],
      },
      saving: false,
    };
  },
  computed: {
    distributionDisplay() {
      return this.distributions.map(distribution => distribution.percentage + '% ').join('- ');
    }
  },
  mounted() {
    this.getValuesFromProps();
  },
  methods: {
    getValuesFromProps() {
      this.form.name = this.name;
      this.form.distributions = this.distributions.map(distribution => {
        return {
          id: distribution.id,
          percentage: distribution.percentage
        };
      });
    },
    setDisplay(value) {
      this.display = value;

      if(!this.display) {
        this.getValuesFromProps();
      }
    },
    async save() {
      this.saving = true;

      const params = {
        id: this.id,
        name: this.form.name,
        distributions: this.form.distributions,
      };
      try{
      
      Swal.fire({title: 'Do you want to save the changes?',showCancelButton: true,})
        .then((result) => {
          /* Read more about isConfirmed, isDenied below */
          if (result.isConfirmed) {
            axios.post('/api/zones/edit', params)
            Swal.fire('Saved!', '', 'success').then(location.reload())
          } else if (result.isDenied) {
            Swal.fire('Changes are not saved', '', 'info')
          }
        })
      }
      catch{
        Swal.fire(
        'Whoooops! something wrong!',
        'refresh the page to see the changes ',
        'error'
      )
        }

      this.$emit('edit', {name: params.name != ""?params.name:"error",distributions:this.form.distributions});

      this.saving = false;
      this.display = true;
    },
    async delete_item() {
      const params = {
        id: this.id
      };
      try{
      
      Swal.fire({
          title: 'Do you want to Delete it?',
          showDenyButton: true,
          confirmButtonText: 'Delete it',
          denyButtonText: `Don't Delete it`,
        }).then((result) => {
          if (result.isConfirmed) {
            axios.post('/api/zones/delete', params).then(Swal.fire('Saved!', '', 'success')).then(location.reload())
          } else if (result.isDenied) {
            Swal.fire('Changes are not saved', '', 'info')
          }
        })
      }
      catch{
        Swal.fire(
        'Whoooops! something wrong!',
        'refresh the page to see the changes ',
        'error'
      )
        }
      this.saving = false;
      this.display = true;
    }
  }
}
</script>

<style type="text/scss" lang="scss">
@import 'resources/scss/variables.scss';

.zone-editable {
  border: 1px solid $gray-color;
  padding: $qmb;
  border-radius: $border-radius;

  .zone-display {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .zone-edit {
    display: flex;
    flex-direction: column;
    gap: $small-action-space;

    .zone-edit-actions {
      display: flex;
      gap: $small-action-space;
      justify-content: end;
    }

    .zone-edit-distributions {
      display: grid;
      grid-template-columns: repeat(1, 1fr);
      gap: $small-action-space;
    }
  }
}
</style>
