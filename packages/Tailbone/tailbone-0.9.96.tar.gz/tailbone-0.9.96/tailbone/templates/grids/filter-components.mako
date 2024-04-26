## -*- coding: utf-8; -*-

<%def name="make_grid_filter_components()">
  ${self.make_grid_filter_numeric_value_component()}
  ${self.make_grid_filter_date_value_component()}
  ${self.make_grid_filter_component()}
</%def>

<%def name="make_grid_filter_numeric_value_component()">
  <script type="text/x-template" id="grid-filter-numeric-value-template">
    <div class="level">
      <div class="level-left">
        <div class="level-item">
          <b-input v-model="startValue"
                   ref="startValue"
                   @input="startValueChanged">
          </b-input>
        </div>
        <div v-show="wantsRange"
             class="level-item">
          and
        </div>
        <div v-show="wantsRange"
             class="level-item">
          <b-input v-model="endValue"
                   ref="endValue"
                   @input="endValueChanged">
          </b-input>
        </div>
      </div>
    </div>
  </script>
  <script>

    const GridFilterNumericValue = {
        template: '#grid-filter-numeric-value-template',
        props: {
            value: String,
            wantsRange: Boolean,
        },
        data() {
            return {
                startValue: null,
                endValue: null,
            }
        },
        mounted() {
            if (this.wantsRange) {
                if (this.value.includes('|')) {
                    let values = this.value.split('|')
                    if (values.length == 2) {
                        this.startValue = values[0]
                        this.endValue = values[1]
                    } else {
                        this.startValue = this.value
                    }
                } else {
                    this.startValue = this.value
                }
            } else {
                this.startValue = this.value
            }
        },
        watch: {
            // when changing from e.g. 'equal' to 'between' filter verbs,
            // must proclaim new filter value, to reflect (lack of) range
            wantsRange(val) {
                if (val) {
                    this.$emit('input', this.startValue + '|' + this.endValue)
                } else {
                    this.$emit('input', this.startValue)
                }
            },
        },
        methods: {
            focus() {
                this.$refs.startValue.focus()
            },
            startValueChanged(value) {
                if (this.wantsRange) {
                    value += '|' + this.endValue
                }
                this.$emit('input', value)
            },
            endValueChanged(value) {
                value = this.startValue + '|' + value
                this.$emit('input', value)
            },
        },
    }

    Vue.component('grid-filter-numeric-value', GridFilterNumericValue)

  </script>
</%def>

<%def name="make_grid_filter_date_value_component()">
  <script type="text/x-template" id="grid-filter-date-value-template">
    <div class="level">
      <div class="level-left">
        <div class="level-item">
          <tailbone-datepicker v-model="startDate"
                               ref="startDate"
                               @input="startDateChanged">
          </tailbone-datepicker>
        </div>
        <div v-show="dateRange"
             class="level-item">
          and
        </div>
        <div v-show="dateRange"
             class="level-item">
          <tailbone-datepicker v-model="endDate"
                               ref="endDate"
                               @input="endDateChanged">
          </tailbone-datepicker>
        </div>
      </div>
    </div>
  </script>
  <script>

    const GridFilterDateValue = {
        template: '#grid-filter-date-value-template',
        props: {
            value: String,
            dateRange: Boolean,
        },
        data() {
            return {
                startDate: null,
                endDate: null,
            }
        },
        mounted() {
            if (this.dateRange) {
                if (this.value.includes('|')) {
                    let values = this.value.split('|')
                    if (values.length == 2) {
                        this.startDate = values[0]
                        this.endDate = values[1]
                    } else {
                        this.startDate = this.value
                    }
                } else {
                    this.startDate = this.value
                }
            } else {
                this.startDate = this.value
            }
        },
        methods: {
            focus() {
                this.$refs.startDate.focus()
            },
            startDateChanged(value) {
                if (this.dateRange) {
                    value += '|' + this.endDate
                }
                this.$emit('input', value)
            },
            endDateChanged(value) {
                value = this.startDate + '|' + value
                this.$emit('input', value)
            },
        },
    }

    Vue.component('grid-filter-date-value', GridFilterDateValue)

  </script>
</%def>

<%def name="make_grid_filter_component()">
  <script type="text/x-template" id="grid-filter-template">

    <div class="level filter" v-show="filter.visible">
      <div class="level-left"
           style="align-items: start;">

        <div class="level-item filter-fieldname">

          <b-field>
            <b-button @click="filter.active = !filter.active"
                      icon-pack="fas"
                      :icon-left="filter.active ? 'check' : null">
              {{ filter.label }}
            </b-button>
          </b-field>

        </div>

        <b-field grouped v-show="filter.active"
                 class="level-item"
                 style="align-items: start;">

          <b-select v-model="filter.verb"
                    @input="focusValue()"
                    class="filter-verb">
            <option v-for="verb in filter.verbs"
                    :key="verb"
                    :value="verb">
              {{ filter.verb_labels[verb] }}
            </option>
          </b-select>

          ## only one of the following "value input" elements will be rendered

          <grid-filter-date-value v-if="filter.data_type == 'date'"
                                  v-model="filter.value"
                                  v-show="valuedVerb()"
                                  :date-range="filter.verb == 'between'"
                                  ref="valueInput">
          </grid-filter-date-value>

          <b-select v-if="filter.data_type == 'choice'"
                    v-model="filter.value"
                    v-show="valuedVerb()"
                    ref="valueInput">
            <option v-for="choice in filter.choices"
                    :key="choice"
                    :value="choice">
              {{ filter.choice_labels[choice] || choice }}
            </option>
          </b-select>

          <grid-filter-numeric-value v-if="filter.data_type == 'number'"
                                    v-model="filter.value"
                                    v-show="valuedVerb()"
                                    :wants-range="filter.verb == 'between'"
                                    ref="valueInput">
          </grid-filter-numeric-value>

          <b-input v-if="filter.data_type == 'string' && !multiValuedVerb()"
                   v-model="filter.value"
                   v-show="valuedVerb()"
                   ref="valueInput">
          </b-input>

          <b-input v-if="filter.data_type == 'string' && multiValuedVerb()"
                   type="textarea"
                   v-model="filter.value"
                   v-show="valuedVerb()"
                   ref="valueInput">
          </b-input>

        </b-field>

      </div><!-- level-left -->
    </div><!-- level -->

  </script>
  <script>

    const GridFilter = {
        template: '#grid-filter-template',
        props: {
            filter: Object
        },

        methods: {

            changeVerb() {
                // set focus to value input, "as quickly as we can"
                this.$nextTick(function() {
                    this.focusValue()
                })
            },

            valuedVerb() {
                /* this returns true if the filter's current verb should expose value input(s) */

                // if filter has no "valueless" verbs, then all verbs should expose value inputs
                if (!this.filter.valueless_verbs) {
                    return true
                }

                // if filter *does* have valueless verbs, check if "current" verb is valueless
                if (this.filter.valueless_verbs.includes(this.filter.verb)) {
                    return false
                }

                // current verb is *not* valueless
                return true
            },

            multiValuedVerb() {
                /* this returns true if the filter's current verb should expose a multi-value input */

                // if filter has no "multi-value" verbs then we safely assume false
                if (!this.filter.multiple_value_verbs) {
                    return false
                }

                // if filter *does* have multi-value verbs, see if "current" is one
                if (this.filter.multiple_value_verbs.includes(this.filter.verb)) {
                    return true
                }

                // current verb is not multi-value
                return false
            },

            focusValue: function() {
                this.$refs.valueInput.focus()
                // this.$refs.valueInput.select()
            }
        }
    }

    Vue.component('grid-filter', GridFilter)

  </script>
</%def>
