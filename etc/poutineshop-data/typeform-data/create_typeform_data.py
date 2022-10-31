import sys
sys.path.append('etc')

import pandas as pd
import numpy as np
import datetime as dt
import random
import lorem
from pydbgen import pydbgen
from common_data_gen import create_ids, create_random_times, create_md5_ids

np.random.seed(10)
random.seed(10)
pydbseed = 10


def typeform_workspace(number_of_workspaces):
    # WORKSPACE
    # id
    # account_id
    # default
    # name
    # shared

    # TEMPORARY LISTS TO BE FILLED IN LATER FOR TABLE CONNECTIONS
    account_id_list = ['account_id_1','account_id_2','account_id_3','account_id_4']
    workspace_names = ['list','of','names']*7
    workspace_id_list = create_ids(number_of_workspaces,10)

    workspace_id = pd.Series(workspace_id_list)
    account_id = pd.Series(np.random.choice(account_id_list, number_of_workspaces))
    default = pd.Series(np.random.choice([True,False], number_of_workspaces))
    name = pd.Series(workspace_names)
    shared = pd.Series(np.random.choice([True, False], size=number_of_workspaces, p=[0.10, 0.90]))

    workspaces = pd.DataFrame({
        'id': workspace_id,
        'account_id': account_id,
        'default': default,
        'name': name,
        'shared': shared
        }
    )

    return workspaces

########################################################################################
def typeform_form_history(form_history_length, workspace_id_list):
    #FORM_HISTORY

    # id - aka form_id
    # theme_id aka y6peYl
    # workspace_id
    # cui_setting_avatar = null
    # cui_setting_is_typing_emulation_disabled = boolean
    # cui_setting_typing_emulation_speed = 'slow','medium','fast'
    # language
    # last_updated_at
    # title
    # type - quiz, form, classification_branching
    # variable_price
    # variable_score

    form_id_list = create_ids(75,8)
    theme_id_list = create_ids(50,6)
    # temporary title list
    title_list = []
    type_list = []
    for i in range(form_history_length):
        title_list.append('temporary_title_'+str(i))
        type_list.append(np.random.choice(['form','quiz','classification_branching']))

    form_id = pd.Series(np.random.choice(form_id_list, form_history_length))
    theme_id = pd.Series(np.random.choice(theme_id_list, form_history_length))
    workspace_id = pd.Series(np.random.choice(workspace_id_list, form_history_length))
    cui_setting_avatar = pd.Series([np.nan]*form_history_length)
    cui_setting_is_typing_emulation_disabled = pd.Series(np.random.choice([True,False], form_history_length, p=[0.65,0.35]))
    cui_setting_typing_emulation_speed = pd.Series(np.random.choice(['slow','medium','fast'], form_history_length))
    # language = pd.Series(np.random.choice(['Francais','English'],form_history_length,p=[0.1,0.9]))
    language = pd.Series([np.nan]*form_history_length)
    last_updated_at = pd.Series(create_random_times(form_history_length))
    title = pd.Series(title_list)
    type = pd.Series(type_list)
    variable_price = pd.Series([np.nan]*form_history_length)
    variable_score = pd.Series(np.random.choice([0,np.nan],form_history_length,p=[0.01,0.99]))

    form_history = pd.DataFrame({
        'id': form_id,
        'theme_id': theme_id,
        'workspace_id': workspace_id,
        'cui_setting_avatar': cui_setting_avatar,
        'cui_setting_is_typing_emulation_disabled': cui_setting_is_typing_emulation_disabled,
        'cui_setting_typing_emulation_speed': cui_setting_typing_emulation_speed,
        'language': language,
        'last_updated_at': last_updated_at,
        'title': title,
        'type': type,
        'variable_price': variable_price,
        'variable_score': variable_score
        }
    )

    return form_history

########################################################################################
def typeform_response_answer_choice(number_of_responses, number_of_answer_choices, response_id):

    ## RESPONSE ANSWER CHOICE
    # response id
    # choice id

    # NOTE: this seems like an enumerated table
    # ex 124k unique response ids, 601 unique choices, 338k table length from client dataset

    response_id_list = response_id
    response_id = pd.Series(response_id)

    choice_id_list = create_ids(number_of_answer_choices, 12)
    choice_id = pd.Series(np.random.choice(choice_id_list, len(response_id)))

    response_answer_choices = pd.DataFrame({
        'response_id': response_id,
        'choice_id': choice_id
        }
    )

    return response_answer_choices

########################################################################################
def typeform_response(number_of_responses, form_id):
    # RESPONSE
    # response_id **
    # form_id FORM_HISTORY
    # calculated_score
    # hidden_*
    # landing_id
    # landed_at
    # metadata_browser
    # metadata_network_id
    # metadata_platform
    # metadata_referer
    # metadata_user_agent
    # submitted_at
    # token_id

    response_id = pd.Series(create_md5_ids(number_of_responses))
    form_id_list = form_id
    form_id = pd.Series(np.random.choice(form_id,number_of_responses))
    calculated_score = pd.Series(np.random.randint(-999,999,number_of_responses))
    hidden_ = pd.Series([np.nan]*number_of_responses)
    landing_id = pd.Series(create_md5_ids(number_of_responses))
    landed_at = pd.Series(create_random_times(number_of_responses))
    submitted_at_list = []
    for i in landed_at:
        random_second = random.randrange(300)
        time = i + dt.timedelta(seconds=random_second)
        submitted_at_list.append(time)
    submitted_at = pd.Series(submitted_at_list)
    metadata_browser = pd.Series([np.nan]*number_of_responses)
    metadata_network_id = pd.Series([np.nan]*number_of_responses)
    metadata_platform = pd.Series([np.nan]*number_of_responses)
    metadata_referer = pd.Series([np.nan]*number_of_responses)
    metadata_user_agent = pd.Series([np.nan]*number_of_responses)
    token_id = pd.Series(create_md5_ids(number_of_responses))


    response = pd.DataFrame({
        'id' : response_id,
        'form_id' : form_id,
        'calculated_score' : calculated_score,
        'hidden_' : hidden_,
        'landing_id' : landing_id,
        'landed_at' : landed_at,
        'metadata_browser' : metadata_browser,
        'metadata_network_id' : metadata_network_id,
        'metadata_platform' : metadata_platform,
        'metadata_referer' : metadata_referer,
        'metadata_user_agent' : metadata_user_agent,
        'submitted_at' : submitted_at,
        'token_id' : token_id
        }
    )


    return response

########################################################################################
def typeform_form_field_history(initial_number, number_of_changes, form_id):

    # FORM_FIELD_HISTORY
    # id
    # form_id FORM_HISTORY
    # form_parent_field_id FORM_FIELD_HISTORY (self-referenced)
        # NOTE: number of changes will include changes in form_field_history to ids (there isn't a timestamp column though...)
    # layout_attachment_property_brightness
    # layout_attachment_property_description
    # layout_attachment_property_focal_point_x
    # layout_attachment_property_focal_point_y
    # layout_attachment_href
    # layout_attachment_scale
    # layout_attachement_type
    # layout_placement
    # layout_type
    # property_allow_multiple_selection
    # property_allow_other_choice
    # property_alphabetical_order
    # property_button_text
    # property_currency
    # property_default_country_code
    # property_description
    # property_hide_marks
    # property_label_center
    # property_label_left
    # property_label_right
    # property_price_type
    # property_price_value
    # property_randomize
    # property_separator
    # property_shape
    # property_show_button
    # property_show_labels
    # property_start_at_one
    # property_structure
    # property_supersized
    # property_vertical_alignment
    # ref
    # title
    # type
    # validation_max_length
    # validation_max_selection
    # validation_max_value
    # validation_min_selection
    # validation_min_value
    # validation_required

    # NOTE:
    # in bch source data, 918 total rows, 818 field_id, 69 form_id
    # title (393 distinct), type (see distinct list below), ref (363 distinct), id and form_id are the only fields without null variables

    #build initial table first
    type_list = ['date','email','group','number','yes_no','dropdown','long_text','statement',
        'short_text','file_upload','phone_number','opinion_scale','WELCOME_SCREEN',
        'picture_choice','THANKYOU_SCREEN','multiple_choice']
    # sample ref = aa9b6d16-67c6-489e-b1a4-77c20d95c49e
    ref_list=[]
    l1 = create_ids(round(initial_number/3),8)
    l2 = create_ids(round(initial_number/3),4)
    l3 = create_ids(round(initial_number/3),4)
    l4 = create_ids(round(initial_number/3),4)
    l5 = create_ids(round(initial_number/3),12)
    for i in range(len(l1)):
        ref_list.append(l1[i]+'-'+l2[i]+'-'+l3[i]+'-'+l4[i]+'-'+l5[i])
    # title has many to many relationship with ref, 1:1 relationship with type (i.e. title doesn't change type)
    temp_title_list = []
    for i in range(round(initial_number/2.5)):
        temp_title_list.append('Temporary title #'+str(i))

    id = pd.Series(create_ids(initial_number,12))

    form_id = pd.Series(np.random.choice(form_id, initial_number))
    form_parent_field_id = pd.Series(np.nan*initial_number)
    type = pd.Series(np.random.choice(type_list, initial_number))
    ref = pd.Series(np.random.choice(ref_list, initial_number))
    title = pd.Series(np.random.choice(temp_title_list, initial_number))

    layout_attachment_property_brightness = pd.Series(np.nan*initial_number)
    layout_attachment_property_description = pd.Series(np.nan*initial_number)
    layout_attachment_property_focal_point_x = pd.Series(np.nan*initial_number)
    layout_attachment_property_focal_point_y = pd.Series(np.nan*initial_number)
    layout_attachment_href = pd.Series(np.nan*initial_number)
    layout_attachment_scale = pd.Series(np.nan*initial_number)
    layout_attachement_type = pd.Series(np.nan*initial_number)
    layout_placement = pd.Series(np.nan*initial_number)
    layout_type = pd.Series(np.nan*initial_number)
    property_allow_multiple_selection = pd.Series(np.nan*initial_number)
    property_allow_other_choice = pd.Series(np.nan*initial_number)
    property_alphabetical_order = pd.Series(np.nan*initial_number)
    property_button_text = pd.Series(np.nan*initial_number)
    property_currency = pd.Series(np.nan*initial_number)
    property_default_country_code = pd.Series(np.nan*initial_number)
    property_description = pd.Series(np.nan*initial_number)
    property_hide_marks = pd.Series(np.nan*initial_number)
    property_label_center = pd.Series(np.nan*initial_number)
    property_label_left = pd.Series(np.nan*initial_number)
    property_label_right = pd.Series(np.nan*initial_number)
    property_price_type = pd.Series(np.nan*initial_number)
    property_price_value = pd.Series(np.nan*initial_number)
    property_randomize = pd.Series(np.nan*initial_number)
    property_separator = pd.Series(np.nan*initial_number)
    property_shape = pd.Series(np.nan*initial_number)
    property_show_button = pd.Series(np.nan*initial_number)
    property_show_labels = pd.Series(np.nan*initial_number)
    property_start_at_one = pd.Series(np.nan*initial_number)
    property_structure = pd.Series(np.nan*initial_number)
    property_supersized = pd.Series(np.nan*initial_number)
    property_vertical_alignment = pd.Series(np.nan*initial_number)
    validation_max_length = pd.Series(np.nan*initial_number)
    validation_max_selection = pd.Series(np.nan*initial_number)
    validation_max_value = pd.Series(np.nan*initial_number)
    validation_min_selection = pd.Series(np.nan*initial_number)
    validation_min_value = pd.Series(np.nan*initial_number)
    validation_required = pd.Series(np.nan*initial_number)

    form_field_history = pd.DataFrame({
        'id' : id,
        'form_id' : form_id,
        'form_parent_field_id' : form_parent_field_id,
        'layout_attachment_property_brightness' : layout_attachment_property_brightness,
        'layout_attachment_property_description' : layout_attachment_property_description,
        'layout_attachment_property_focal_point_x' : layout_attachment_property_focal_point_x,
        'layout_attachment_property_focal_point_y' : layout_attachment_property_focal_point_y,
        'layout_attachment_href' : layout_attachment_href,
        'layout_attachment_scale' : layout_attachment_scale,
        'layout_attachement_type' : layout_attachement_type,
        'layout_placement' : layout_placement,
        'layout_type' : layout_type,
        'property_allow_multiple_selection' : property_allow_multiple_selection,
        'property_allow_other_choice' : property_allow_other_choice,
        'property_alphabetical_order' : property_alphabetical_order,
        'property_button_text' : property_button_text,
        'property_currency' : property_currency,
        'property_default_country_code' : property_default_country_code,
        'property_description' : property_description,
        'property_hide_marks' : property_hide_marks,
        'property_label_center' : property_label_center,
        'property_label_left' : property_label_left,
        'property_label_right' : property_label_right,
        'property_price_type' : property_price_type,
        'property_price_value' : property_price_value,
        'property_randomize' : property_randomize,
        'property_separator' : property_separator,
        'property_shape' : property_shape,
        'property_show_button' : property_show_button,
        'property_show_labels' : property_show_labels,
        'property_start_at_one' : property_start_at_one,
        'property_structure' : property_structure,
        'property_supersized' : property_supersized,
        'property_vertical_alignment' : property_vertical_alignment,
        'ref' : ref,
        'title' : title,
        'type' : type,
        'validation_max_length' : validation_max_length,
        'validation_max_selection' : validation_max_selection,
        'validation_max_value' : validation_max_value,
        'validation_min_selection' : validation_min_selection,
        'validation_min_value' : validation_min_value,
        'validation_required' : validation_required
        }
    )
    return form_field_history

########################################################################################
def typeform_response_answer(number_of_answers, response_id, field_id, form_id):

    # RESPONSE ANSWER
    # response_id** RESPONSE
    # field_id FORM_FIELD_HISTORY
    # form_id FORM_HISTORY
    # _boolean
    # date
    # email
    # file_url
    # number
    # payment_amount
    # payment_last_4
    # payment_name
    # text
    # type
    # url

    # NOTE:
    # in bch source data, 585771 answers, 161920 response_id, 284 field_id, 58 form_id

    response_id = pd.Series(np.random.choice(response_id, number_of_answers))
    field_id = pd.Series(np.random.choice(field_id, number_of_answers))
    form_id = pd.Series(np.random.choice(form_id, number_of_answers))
    _boolean = pd.Series(np.random.choice(['null','false','true'],number_of_answers, p=[0.45,0.25,0.30]))
    date = pd.Series(create_random_times(number_of_answers))
    myDB=pydbgen.pydb(seed=pydbseed)
    email_list = myDB.gen_data_series(round(len(response_id)/5),data_type='email')
    email = pd.Series(np.random.choice(email_list, number_of_answers))
    file_url = pd.Series(np.nan * number_of_answers)
    number_list = np.random.randint(range(0,30),number_of_answers)
    for i in number_list:
        if 11 > i < 18 or 22 > i < 25:
            number_list[i] = 99999
    number = pd.Series(number_list)
    payment_amount  = pd.Series(np.nan * number_of_answers)
    payment_last_4 = pd.Series(np.nan * number_of_answers)
    payment_name = pd.Series(np.nan * number_of_answers)
    type_list = [ 'choice', 'text', 'email', 'phone_number', 'choices', 'number', 'boolean', 'date', 'file_url' ]
    type = pd.Series(np.random.choice(type_list, number_of_answers))
    # create text values for choice and text types only
    text = pd.Series(np.nan * number_of_answers)
    for i in range(number_of_answers):
        if type[i] in ['choice','text']:
            text[i] = np.random.choice(lorem.text().split())
    url = pd.Series(np.nan * number_of_answers)

    response_answer = pd.DataFrame({
        'response_id': response_id,
        'field_id': field_id,
        'form_id': form_id,
        '_boolean': _boolean,
        'date': date,
        'email': email,
        'file_url': file_url,
        'number': number,
        'payment_amount': payment_amount,
        'payment_last_4': payment_last_4,
        'payment_name': payment_name,
        'text': text,
        'type': type,
        'url': url
        }
    )

    return response_answer

########################################################################################
def typeform_form_field_choice_history(number_of_mods, choice_id, form_id, field_id):
    # FORM FIELD CHOICE HISTORY
    # id
    # form_id
    # field_id FORM_FIELD_HISTORY
    # attachment_href
    # attachment_property_description
    # attachment_type
    # label
    # ref
    # not_null: id, field_id, form_id, label, ref
    # distinct: id

    id = pd.Series(choice_id)
    form_id = pd.Series(np.random.choice(form_id, number_of_mods))
    attachment_href = pd.Series(np.nan * number_of_mods)
    attachment_property_description = pd.Series(np.nan * number_of_mods)
    attachment_type = pd.Series(np.nan * number_of_mods)
    label_list = ['Ontario','Quebec','Nova Scotia','British Columbia','Portugal','Brazil',
        'Kenya','India','Nigeria','I Accept','I Decline','Talk Now','Not Yet', 'Something Else',
        'Yes','No','Fries','Cheese','Gravy','Need more information']
    label = pd.Series(np.random.choice(label_list,number_of_mods))
    attachment_href = pd.Series(np.nan * number_of_mods)
    attachment_property_description = pd.Series(np.nan * number_of_mods)
    attachment_type = pd.Series(np.random.choice(['null','image'],number_of_mods,p=[0.95,0.05]))

    ref_list=[]
    l1 = create_ids(round(round(number_of_mods/2)),8)
    l2 = create_ids(round(round(number_of_mods/2)),4)
    l3 = create_ids(round(round(number_of_mods/2)),4)
    l4 = create_ids(round(round(number_of_mods/2)),4)
    l5 = create_ids(round(round(number_of_mods/2)),2)
    for i in range(len(l1)):
        ref_list.append(l1[i]+'-'+l2[i]+'-'+l3[i]+''+l4[i]+'-'+l5[i])
    ref = pd.Series(np.random.choice(ref_list, number_of_mods))

    form_field_choice_history = pd.DataFrame({
        'id' : id,
        'form_id' : form_id,
        'field_id' : field_id,
        'attachment_href' : attachment_href,
        'attachment_property_description' : attachment_property_description,
        'attachment_type' : attachment_type,
        'label' : label
        # 'ref' : ref
        }
    )

    return form_field_choice_history

########################################################################################
workspace = typeform_workspace(number_of_workspaces=21)
form_history = typeform_form_history(200, workspace['id'])
response = typeform_response(1000,form_history['id'])
response_answer_choice = typeform_response_answer_choice(number_of_responses = 7800, number_of_answer_choices=120, response_id = response['id'])
form_field_history = typeform_form_field_history(initial_number = 400, number_of_changes = 200, form_id = form_history['id'])
response_answer = typeform_response_answer(number_of_answers = 5000, response_id = response['id'], form_id = form_history['id'], field_id = form_field_history['id'] )
form_field_choice_history = typeform_form_field_choice_history(number_of_mods = len(response_answer_choice['choice_id'].unique()), choice_id = response_answer_choice['choice_id'].unique(), form_id = form_history['id'], field_id = form_field_history['id'])

workspace.to_csv('etc/typeform-data/workspace.csv')
form_history.to_csv('etc/typeform-data/form_history.csv')
response.to_csv('etc/typeform-data/response.csv')
response_answer_choice.to_csv('etc/typeform-data/response_answer_choice.csv')
form_field_history.to_csv('etc/typeform-data/form_field_history.csv')
response_answer.to_csv('etc/typeform-data/response_answer.csv')
form_field_choice_history.to_csv('etc/typeform-data/form_field_choice_history.csv')
