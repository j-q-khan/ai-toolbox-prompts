# Full code: Vikunja Tutorial: Projects, Kanban and Gantt

Written from Vikunja's Quick Add Magic, filters, views, task relations and import help pages, checked 2026-11-05 and re-checked 2026-11-06 (Vikunja v2.8.0). Made-up example tasks; paste into a test list first. Not run by us.

### garden-plan.txt (paste into Quick Add Magic at the top of a list's List view; indented lines become subtasks)
```
Measure the garden *planning !3 this weekend
Buy supplies *shopping !4 next week
  Compost and soil *shopping
  Seeds and bulbs *shopping
Clear the old beds *outdoor !2 next monday
Plant the first bed *outdoor !3 in 14 days
Water the new plants *outdoor every 3 days
Ask a neighbour to water the plants *"waiting on others" !2
```

### Four filters (List or Table view filter box, or New Saved Filter; web field names)
```
done = false && priority in 4, 5
done = false && labels in "waiting on others"
done = false && labels in shopping, outdoor
done = false && dueDate [TYPE THE LESS-THAN SIGN HERE] now
```

### Filter notes (read before pasting the last filter)
```
Last filter: delete [TYPE THE LESS-THAN SIGN HERE], brackets too, and type
the less-than sign in its place (on US and UK keyboards, Shift and comma).
It must read: dueDate, a space, the sign, a space, now. Vikunja has no word
for it, so it won't run as pasted; a YouTube description can't hold the sign.
Or copy "Undone overdue tasks" from vikunja.io/help/filters, ready-made.
Saved filters: switch off "Include Tasks which don't have a value set", or tasks with no value show up too.
Labels with spaces need quotes, as in the second filter.
```

### Kanban board setup (Kanban tab)
```
1. Buckets: To Do, In Progress, Waiting, Done (type a new name in the field at the far right)
2. Done bucket: open the Done column's three-dot menu and choose Done bucket
3. Default bucket: same menu on To Do, choose Default bucket, so new tasks land there
4. WIP limit: same menu on In Progress, Limit, type 3; when full, it refuses new cards
5. Gantt tab: give each task a start and an end date. For arrows between tasks,
   open a task, find Relations in its right sidebar, click Add a relation,
   pick the other task and choose Blocked by (or Precedes)
```

### template.csv (for Settings, then Import, then CSV; the project column makes sub-lists)
```
title,description,project,labels,start_date,end_date,due_date,priority
Measure the garden,Front and back,Planning,planning,2026-11-07,2026-11-08,2026-11-08,3
Buy supplies,Compost and seeds,Shopping,"shopping,outdoor",2026-11-09,2026-11-14,2026-11-14,4
Plant the first bed,,Planting,outdoor,2026-11-15,2026-11-21,2026-11-21,3
```
