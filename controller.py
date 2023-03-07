import model
import view


def button_click():
    while True:
        command = view.start_selection()
        notes = model.extract_csv()
        if command == 1:
            note = view.create_note()
            if len(notes) > 0:
                id = len(notes) + 1
            else:
                id = 1
            note.update({str(id): 'ID'})
            notes.append(note)
            model.write_csv(notes)
            view.confirm()
        elif command == 2:
            try:
                note = model.search_for_id(view.get_id(), notes)
                view.print_note(note)
                view.confirm()
            except:
                view.not_find()
        elif command == 3:
            try:
                date = view.get_date()
                result = model.sort_for_date(date, notes)
                for note in result:
                    view.print_note(note)
                view.confirm()
            except:
                view.not_find()
        elif command == 4:
            try:
                id = view.get_id()
                note = model.search_for_id(id, notes)
                view.print_note(note)
                notes.remove(note)
                note = view.create_note()
                note.update({'ID': id})
                notes.append(note)
                model.write_csv(notes)
                view.confirm()
            except:
                view.not_find()
        elif command == 5:
            try:
                id = view.get_id()
                model.delete_for_id(id, notes)
                model.write_csv(notes)
                view.confirm()
            except:
                view.not_find()
        elif command == 6:
            try:
                for note in notes:
                    view.print_note(note)
                view.confirm()
            except:
                view.not_find()
        else:
            return