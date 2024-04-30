### 0.0.1
OG

### 0.0.2
Only updates attribute (and adds to tracked_attributes) if the new value is different

### 0.0.3
Keeps track of removed items from collections (list, set, dict)

### 0.0.4
Slight optimizations. Only checks for collections if attribute has added _r. Only checks whether
the attribute changed before adding to tracked_attributes if attribute has _d.