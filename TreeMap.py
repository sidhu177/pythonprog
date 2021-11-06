# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 22:10:37 2018

Taken from Data Structures and Algorithms using Python
"""

class TreeMap(LinkedBinaryTree, MapBase):
    class Position(LinkedBinaryTree.Position):
        def key(self):
            return self.element()._key
            
        def value(self):
            return self.element()._value
            
        def _subtree_search(self,p,k):
            if k==p.key():
                return p
            elif k<p.key():
                if self.left(p) is not None:
                    return self._subtree_search(self.left(p),k)
                else:
                    if self.right(p) is not None:
                        return self._subtree_search(self.right(p),k)
                return p
                
        def _subtree_first_position(self,p):
            walk = p
            while self.left(walk) is not None:
                walk = self.left(walk)
            return walk
            
        def _subtree_last_position(self,p):
            walk = p
            while self.right(walk) is not None:
                walk = self.right(walk)
            return walk
            
        def first(self):
            return self._subtree_first_position(self.root()) if len(self)>0 else None
            
        def last(self):
            return self._subtree_last_position(self.root()) if len(self)>0 else None
            
        def before(self,p):
            self._validate(p)
            if self.left(p):
                return self._subtree_last_position(self.left(p))
            else:
                walk = p
                above = self.parent(walk)
                while above is not None and walk == self.left(above):
                    walk = above
                    above = self.parent(walk)
                return above
                
        def after(self,p):
            def find_position(self,k):
                if self.is_empty():
                    return None
                else:
                    p = self._subtree_search(self.root(),k)
                    self._rebalance_access(p)
                    return p
                    
        def find_min(self):
            if self.is_empty():
                return None
            else:
                p = self.first()
                return (p.key(),p.value())
                
        def find_ge(self,k):
            if self.is_empty():
                return None
            else:
                p = self.find_position(k)
                if p.key() < k:
                    p = self.after(p)
                return (p.key(),p.value()) if p is not None else None
                
                
        def find_range(self,start,stop):
            if not self.is_empty():
                if start is None:
                    p = self.first()
                else:
                    p = self.fin_position(start)
                    if p.key()<start:
                        p=self.after(p)
                while p is not None and (stop is None or p.key() < stop):
                    yield (p.key(), p.value())
                    p = self.after(p)
                    
        
        def __getitem__(self,k):
            if self.is_empty():
                raise KeyError('Key Error: '+ repr(k))
            else:
                p = self._subtree_search(self.root(),k)
                self._rebalance_access(p)
                if k!=p.key():
                    raise KeyError('Key Error: ' + repr(k))
                return p.value()
                
        def __setitem__(self,k,v):
            if self.is_empty():
                leaf = self._add_root(self._Item(k,v))
            else:
                p = self._subtree_search(self.root(),k)
                if p.key()==k:
                    p.element()._value = v
                    self._rebalance_access(p)
                    return
                else:
                    item = self._Item(k,v)
                    if p.key()<k:
                        leaf = self._add_right(p, item)
                    else:
                        leaf = self._add_left(p, item)
            self._rebalance_insert(leaf)
            
        def __iter__(self):
            p = self.first()
            while p is not None:
                yield p.key()
                p = self.after(p)
                
        def delete(self,p):
            self._validate(p)
            if self.left(p) and self.right(p):
                replacement = self._subtree_last_position(self.left(p))
                self._replace(p, replacement.element())
                p = replacement
            parent  = self.parent(p)
            self._delete(p)
            self._rebalance_delete(parent)
            
        def __delitem__(self,k):
            if not self.is_empty():
                p = self._subtree_search(self.root(),k)
                if k==p.key():
                    self.delete(p)
                    return
                self._rebalance_access(p)
            raise KeyError('Key Error: '+ repr(k))
            
        def _relink(self,parent,child,make_left_child):
            if make_left_child:
                parent._left = child
            else:
                parent._right = child
            if child is not None:
                child._parent = parent
                
        def _rotate(self,p):
            x = p._node
            y = x._parent
            z = y._parent
            if z is None:
                self._root = x
                x._parent = None
            else:
                self._relink(z,x,y == z._left)
            if x==y.left:
                self._relink(y,x._right, True)
                self._relink(x,y,False)
            else:
                self._relink(y,x._left,False)
                self._relink(x,y,True)
                
        def _restructure(self,x):
            y = self.parent(x)
            z = self.parent(y)
            if (x==self.right(y))==(y=self.right(z)):
                self._rotate(y)
                return y
            else:
                self._rotate(x)
                self._rotate(x)
                return x