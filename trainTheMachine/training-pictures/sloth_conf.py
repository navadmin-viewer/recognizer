# This is sloth's configuration created for annotating ground truth for training models for NAVADMIN Viewer - Uniform Recognizer
#by Anson Liu
#
# LABELS
#
# List/tuple of dictionaries that defines the label classes
# that are handled by sloth.  For each label, there should
# be one dictionary that contains the following keys:
#
#   - 'item' : Visualization item for this label. This can be
#              any python callable or a module path string 
#              implementing the visualization item interface.
#
#   - 'inserter' : (optional) Item inserter for this label.
#                  If the user selects to insert a new label of this class
#                  the inserter is responsible to actually 
#                  capture the users mouse actions and insert
#                  a new label into the annotation model.
#
#   - 'hotkey' : (optional) A keyboard shortcut starting 
#                the insertion of a new label of this class.
#
#   - 'attributes' : (optional) A dictionary that defines the
#                    keys and possible values of this label
#                    class.
#
#   - 'text' : (optional) A label for the item's GUI button.

# LABEL FORMAT - type_version:item_name:color:size
# Names taken from https://www.public.navy.mil/bupers-npc/support/uniforms/uniformregulations/Pages/NavyAwardsPrecedenceChart.aspx
# Strip suffix ribbon/medal from listed name if listed that way. 

# To download all image files from site wget -nd -r -P ./ -A jpeg,jpg,bmp,gif,png http://XXX
# Stock images put in stockImages folder

LABELS = (
     {"attributes": {"type":  "rectangle",
                    "class": "badge",
                    "label":    [
                        "badge:presidential_service",
                        "badge:vice_presidential_service",
                        "badge:office_of_secretary_of_defense",
                        "badge:joint_chiefs_of_staff",
                        "badge:command_senior_enlisted_leader",
                        "badge:recruiting_command",
                        "badge:career_counselor",
                        "badge:recruit_division_command_badge",
                        "badge:gold_wreath_award",
                        "badge:merchant_marine_service_emblem",
                        "badge:navy_security_forces",
                        "badge:office_of_secretary_of_defense",
                        "badge:correction_specialist",
                        "badge:office_of_secretary_of_defense",
                        "badge:chief_master_at_arms"
                    ]},
     "item":     "sloth.items.RectItem",
     "inserter": "sloth.items.RectItemInserter",
     "hotkey": "q",
     "text":     "Badges"
    },
    {"attributes": {"type":  "rectangle",
                    "class": "insignia",
                    "label":    [
                        "insignia:naval_astronaut_insignia:gold",
                        "insignia:naval_astonaut_nfo_insignia:gold",
                        "insignia:naval_aviator_insignia:gold",
                        "insignia:naval_aviation_observer_and_flight_meteorologist_insignia:gold",
                        "insignia:meteorologists:gold",
                        "insignia:naval_flight_surgeon_insignia:gold",
                        "insignia:naval_flight_nurse:gold",
                        "insignia:naval_flight_officer:gold",
                        "insignia:professional_avation_maintenance_officer:gold",
                        "insignia:aerospace_experimental_psychologist_and_aerospace_physiologist:gold",
                        "insignia:aviation_warfare_specialist:silver",
                        "insignia:naval_aviation_supply_corps:gold",
                        "insignia:naval_aircrew_warfare_specialist:silver",
                        "insignia:explosive_ordnance_disposal_officer:gold",
                        "insignia:master_explosive_ordnance_disposal_officer:silver",
                        "insignia:senior_explosive_ordnance_disposal_officer:silver",
                        "insignia:basic_explosive_ordnance_disposal_officer:silver",
                        "insignia:fleet_marine_force_officer:gold",
                        "insignia:fleet_marine_force_enlisted_warfare_specialist:silver",
                        "insignia:seabee_combat_warfare_officer:gold",
                        "insignia:seabee_combat_warfare_enlisted:silver",
                        "insignia:special_warfare_insignia:gold",
                        "insignia:master_special_warfare_combatant-craft:silver",
                        "insignia:senior_special_warfare_combatant-craft:silver",
                        "insignia:basic_special_warfare_combatant-craft:silver",
                        "insignia:submarine_officer:gold",
                        "insignia:submarine_enlisted_warfare_specialist:silver",
                        "insignia:submarine_medical:gold",
                        "insignia:submarine_engineer_duty:gold",
                        "insignia:submarine_supply:gold",
                        "insignia:surface_warfare_officer:gold",
                        "insignia:surface_enlisted_warfare_specialist:silver",
                        "insignia:surface_warfare_dental_corps:gold",
                        "insignia:surface_warfare_medical_corps:gold",
                        "insignia:surface_warfare_medical_service_corps:gold",
                        "insignia:surface_warfare_nurse_corps:gold",
                        "insignia:surface_warfare_supply_corps:gold",
                        "insignia:marine_corps_combat_aircrew:gold",
                        "insignia:integrated_undersea_surveillance_system_officer:gold",
                        "insignia:integrated_undersea_surveillance_system_enlisted:silver",
                        "insignia:small_craft_officer_in_charge:gold",
                        "insignia:small_craft_petty_officer_in_charge:silver",
                        "insignia:craftmaster:gold",
                        "insignia:naval_parachutist:gold",
                        "insignia:basic_parachutist:silver",
                        "insignia:submarine_combat_patrol:silver",
                        "insignia:ssbn_deterrent_patrol_20:gold",
                        "insignia:ssbn_deterrent_patrol:silver",
                        "insignia:diving_officer:gold",
                        "insignia:diving_medical:gold",
                        "insignia:master_diver:silver",
                        "insignia:diving_medical_technician:silver",
                        "insignia:first_class_diver:silver",
                        "insignia:second_class_diver:silver",
                        "insignia:scuba_diver:silver",
                        "insignia:deep_submergence:gold",
                        "insignia:information_warfare_officer:gold",
                        "insignia:enlisted_information_warfare_specialist:silver",
                        "insignia:nuclear_weapons_security:silver",
                        "insignia:navy_expeditionary_supply_corps_officer:gold",
                        "insignia:enlisted_expeditionary_warfare_specialist:silver",
                        "insignia:strategic_sealift_officer_warfare:gold",
                        "insignia:marine_corps_combatant_diver:gold",
                        "insignia:engineering_duty_officer:gold",
                        "insignia:command_at_sea:gold",
                        "insignia:command_ashore_project_manager_insignia:gold"
                    ]},
     "item":     "sloth.items.RectItem",
     "inserter": "sloth.items.RectItemInserter",
     "hotkey": "w",
     "text":     "Insignia"
    },
    {"attributes": {"type":  "rectangle",
                    "class": "medal",
                    "label":    [
                        "medal:medal_of_honor",
                        "medal:navy_cross",
                        "medal:distinguished_service_cross", 
                        "medal:defense_distinguished_service",
                        "medal:army_distinguished_service", 
                        "medal:navy_distinguished_service", 
                        "medal:silver_star",
                        "medal:defense_superior_service",
                        "medal:legion_of_merit",
                        "medal:distinguished_flying_cross",
                        "medal:soldier's_medal", 
                        "medal:navy_and_marine_corps",
                        "medal:bronze_star",
                        "medal:purple_heart",
                        "medal:defense_meritorious_service",
                        "medal:meritorious_service",
                        "medal:air",
                        "medal:aerial_achievement",
                        "medal:joint_service_commendation",
                        "medal:army_commendation",
                        "medal:navy_and_marine_corps_commendation",
                        "medal:joint_service_achievement",
                        "medal:army_achievement",
                        "medal:navy_and_marine_corps_achievement", 
                        "medal:combat_action",
                        "medal:presidential_unit_citation",
                        "medal:joint_meritorious_unit_award",
                        "medal:navy_unit_commendation",
                        "medal:army_meritorious_unit_commendation",
                        "medal:navy_meritorious_unit_commendation",
                        "medal:coast_guard_meritorious_unit_commendation",
                        "medal:navy_e",
                        "medal:prisoner_of_war",
                        "medal:army_good_conduct",
                        "medal:navy_good_conduct",
                        "medal:coast_guard_good_conduct",
                        "medal:navy_reserve_meritorious_service",
                        "medal:navy_fleet_marine_force",
                        "medal:navy_expeditionary",
                        "medal:national_defense_service",
                        "medal:korean_service",
                        "medal:antarctica_service",
                        "medal:armed_forces_expeditionary",
                        "medal:vietnam_service",
                        "medal:southwest_asia_service",
                        "medal:kosovo_campaign",
                        "medal:afghanistan_campaign",
                        "medal:iraq_campaign",
                        "medal:inherent_resolve_campaign",
                        "medal:global_war_on_terrorism_expeditionary_service",
                        "medal:global_war_on_terrorism_service",
                        "medal:korea_defense_service",
                        "medal:armed_forces_service",
                        "medal:humanitarian_service",
                        "medal:military_outstanding_volunteer_service",
                        "medal:sea_service_deployment",
                        "medal:coast_guard_special_operations_service",
                        "medal:coast_guard_sea_service",
                        "medal:navy_arctic_service",
                        "medal:navy_reserve_sea_service",
                        "medal:navy_marine_corps_overseas",
                        "medal:navy_recruiting_service",
                        "medal:navy_recruit_training_service",
                        "medal:navy_ceremonial_guard_service",
                        "medal:navy_basic_military_training_honor_graduate",
                        "medal:armed_forces_reserve",
                        "medal:navy_reserve",
                        "medal:philippine_presidential_unit_citation",
                        "medal:republic_of_korea_presidential_unit_citation",
                        "medal:republic_of_vietnam_presidential_unit_citation",
                        "medal:republic_of_vietnam_gallantry_cross_unit_citation",
                        "medal:republic_of_vietnam_mertitorious_unit_citation_action",
                        "medal:united_nations_service",
                        "medal:united_nations",
                        "medal:nato",
                        "medal:nato_kosovo",
                        "medal:nato_afghanistan",
                        "medal:multinational_force_and_observers",
                        "medal:inter_american_defense_board",
                        "medal:republic_of_vietnam_campaign",
                        "medal:kuwait_liberation_medal_kingdom_of_saudi_arabia",
                        "medal:kuwait_liberation_medal_kuwait",
                        "medal:rifle_marksmanship",
                        "medal:pistol_marksmanship"
                    ]},
     "item":     "sloth.items.RectItem",
     "inserter": "sloth.items.RectItemInserter",
     "hotkey": "e",
     "text":     "Medals"
    },
    {"attributes": {"type":  "rectangle",
                    "class": "ribbon",
                    "label":    [
                        "ribbon:medal_of_honor",
                        "ribbon:navy_cross",
                        "ribbon:distinguished_service_cross", 
                        "ribbon:defense_distinguished_service",
                        "ribbon:army_distinguished_service", 
                        "ribbon:navy_distinguished_service", 
                        "ribbon:silver_star",
                        "ribbon:defense_superior_service",
                        "ribbon:legion_of_merit",
                        "ribbon:distinguished_flying_cross",
                        "ribbon:soldier's_medal", 
                        "ribbon:navy_and_marine_corps",
                        "ribbon:bronze_star",
                        "ribbon:purple_heart",
                        "ribbon:defense_meritorious_service",
                        "ribbon:meritorious_service",
                        "ribbon:air",
                        "ribbon:aerial_achievement",
                        "ribbon:joint_service_commendation",
                        "ribbon:army_commendation",
                        "ribbon:navy_and_marine_corps_commendation",
                        "ribbon:joint_service_achievement",
                        "ribbon:army_achievement",
                        "ribbon:navy_and_marine_corps_achievement", 
                        "ribbon:combat_action",
                        "ribbon:presidential_unit_citation",
                        "ribbon:joint_meritorious_unit_award",
                        "ribbon:navy_unit_commendation",
                        "ribbon:army_meritorious_unit_commendation",
                        "ribbon:navy_meritorious_unit_commendation",
                        "ribbon:coast_guard_meritorious_unit_commendation",
                        "ribbon:navy_e",
                        "ribbon:prisoner_of_war",
                        "ribbon:army_good_conduct",
                        "ribbon:navy_good_conduct",
                        "ribbon:coast_guard_good_conduct",
                        "ribbon:navy_reserve_meritorious_service",
                        "ribbon:navy_fleet_marine_force",
                        "ribbon:navy_expeditionary",
                        "ribbon:national_defense_service",
                        "ribbon:korean_service",
                        "ribbon:antarctica_service",
                        "ribbon:armed_forces_expeditionary",
                        "ribbon:vietnam_service",
                        "ribbon:southwest_asia_service",
                        "ribbon:kosovo_campaign",
                        "ribbon:afghanistan_campaign",
                        "ribbon:iraq_campaign",
                        "ribbon:inherent_resolve_campaign",
                        "ribbon:global_war_on_terrorism_expeditionary_service",
                        "ribbon:global_war_on_terrorism_service",
                        "ribbon:korea_defense_service",
                        "ribbon:armed_forces_service",
                        "ribbon:humanitarian_service",
                        "ribbon:military_outstanding_volunteer_service",
                        "ribbon:sea_service_deployment",
                        "ribbon:coast_guard_special_operations_service",
                        "ribbon:coast_guard_sea_service",
                        "ribbon:navy_arctic_service",
                        "ribbon:navy_reserve_sea_service",
                        "ribbon:navy_marine_corps_overseas",
                        "ribbon:navy_recruiting_service",
                        "ribbon:navy_recruit_training_service",
                        "ribbon:navy_ceremonial_guard_service",
                        "ribbon:navy_basic_military_training_honor_graduate",
                        "ribbon:armed_forces_reserve",
                        "ribbon:navy_reserve",
                        "ribbon:philippine_presidential_unit_citation",
                        "ribbon:republic_of_korea_presidential_unit_citation",
                        "ribbon:republic_of_vietnam_presidential_unit_citation",
                        "ribbon:republic_of_vietnam_gallantry_cross_unit_citation",
                        "ribbon:republic_of_vietnam_mertitorious_unit_citation_action",
                        "ribbon:united_nations_service",
                        "ribbon:united_nations",
                        "ribbon:nato",
                        "ribbon:nato_kosovo",
                        "ribbon:nato_afghanistan",
                        "ribbon:multinational_force_and_observers",
                        "ribbon:inter_american_defense_board",
                        "ribbon:republic_of_vietnam_campaign",
                        "ribbon:kuwait_liberation_medal_kingdom_of_saudi_arabia",
                        "ribbon:kuwait_liberation_medal_kuwait",
                        "ribbon:rifle_marksmanship",
                        "ribbon:pistol_marksmanship"
                    ]},
     "item":     "sloth.items.RectItem",
     "inserter": "sloth.items.RectItemInserter",
     "hotkey": "r",
     "text":     "Ribbons"
    }
)

# HOTKEYS
#
# Defines the keyboard shortcuts.  Each hotkey is defined by a tuple
# with at least 2 entries, where the first entry is the hotkey (sequence),
# and the second entry is the function that is called.  The function
# should expect a single parameter, the labeltool object.  The optional
# third entry -- if present -- is expected to be a string describing the 
# action.
HOTKEYS = (
    ('Space',     [lambda lt: lt.currentImage().confirmAll(),
                   lambda lt: lt.currentImage().setUnlabeled(False),
                   lambda lt: lt.gotoNext()
                  ],                                         'Mark image as labeled/confirmed and go to next'),
    ('Backspace', lambda lt: lt.gotoPrevious(),              'Previous image/frame'),
    ('PgDown',    lambda lt: lt.gotoNext(),                  'Next image/frame'),
    ('PgUp',      lambda lt: lt.gotoPrevious(),              'Previous image/frame'),
    ('Tab',       lambda lt: lt.selectNextAnnotation(),      'Select next annotation'),
    ('Shift+Tab', lambda lt: lt.selectPreviousAnnotation(),  'Select previous annotation'),
    ('Ctrl+f',    lambda lt: lt.view().fitInView(),          'Fit current image/frame into window'),
    ('Del',       lambda lt: lt.deleteSelectedAnnotations(), 'Delete selected annotations'),
    ('ESC',       lambda lt: lt.exitInsertMode(),            'Exit insert mode'),
    ('Shift+l',   lambda lt: lt.currentImage().setUnlabeled(False), 'Mark current image as labeled'),
    ('Shift+c',   lambda lt: lt.currentImage().confirmAll(), 'Mark all annotations in image as confirmed'),
)

# CONTAINERS
#
# A list/tuple of two-tuples defining the mapping between filename pattern and
# annotation container classes.  The filename pattern can contain wildcards
# such as * and ?.  The corresponding container is expected to either a python
# class implementing the sloth container interface, or a module path pointing
# to such a class.
CONTAINERS = (
    ('*.json',       'sloth.annotations.container.JsonContainer'),
    ('*.msgpack',    'sloth.annotations.container.MsgpackContainer'),
    ('*.yaml',       'sloth.annotations.container.YamlContainer'),
    ('*.pickle',     'sloth.annotations.container.PickleContainer'),
    ('*.sloth-init', 'sloth.annotations.container.FileNameListContainer'),
)

# PLUGINS
#
# A list/tuple of classes implementing the sloth plugin interface.  The
# classes can either be given directly or their module path be specified 
# as string.
PLUGINS = (
)


