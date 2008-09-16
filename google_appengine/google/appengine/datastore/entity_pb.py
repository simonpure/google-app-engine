#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.net.proto import ProtocolBuffer
import array
import dummy_thread as thread

__pychecker__ = """maxreturns=0 maxbranches=0 no-callinit
                   unusednames=printElemNumber,debug_strs no-special"""

class PropertyValue_ReferenceValuePathElement(ProtocolBuffer.ProtocolMessage):
  has_type_ = 0
  type_ = ""
  has_id_ = 0
  id_ = 0
  has_name_ = 0
  name_ = ""

  def __init__(self, contents=None):
    if contents is not None: self.MergeFromString(contents)

  def type(self): return self.type_

  def set_type(self, x):
    self.has_type_ = 1
    self.type_ = x

  def clear_type(self):
    self.has_type_ = 0
    self.type_ = ""

  def has_type(self): return self.has_type_

  def id(self): return self.id_

  def set_id(self, x):
    self.has_id_ = 1
    self.id_ = x

  def clear_id(self):
    self.has_id_ = 0
    self.id_ = 0

  def has_id(self): return self.has_id_

  def name(self): return self.name_

  def set_name(self, x):
    self.has_name_ = 1
    self.name_ = x

  def clear_name(self):
    self.has_name_ = 0
    self.name_ = ""

  def has_name(self): return self.has_name_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_type()): self.set_type(x.type())
    if (x.has_id()): self.set_id(x.id())
    if (x.has_name()): self.set_name(x.name())

  def Equals(self, x):
    if x is self: return 1
    if self.has_type_ != x.has_type_: return 0
    if self.has_type_ and self.type_ != x.type_: return 0
    if self.has_id_ != x.has_id_: return 0
    if self.has_id_ and self.id_ != x.id_: return 0
    if self.has_name_ != x.has_name_: return 0
    if self.has_name_ and self.name_ != x.name_: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_type_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: type not set.')
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthString(len(self.type_))
    if (self.has_id_): n += 2 + self.lengthVarInt64(self.id_)
    if (self.has_name_): n += 2 + self.lengthString(len(self.name_))
    return n + 1

  def Clear(self):
    self.clear_type()
    self.clear_id()
    self.clear_name()

  def OutputUnchecked(self, out):
    out.putVarInt32(122)
    out.putPrefixedString(self.type_)
    if (self.has_id_):
      out.putVarInt32(128)
      out.putVarInt64(self.id_)
    if (self.has_name_):
      out.putVarInt32(138)
      out.putPrefixedString(self.name_)

  def TryMerge(self, d):
    while 1:
      tt = d.getVarInt32()
      if tt == 116: break
      if tt == 122:
        self.set_type(d.getPrefixedString())
        continue
      if tt == 128:
        self.set_id(d.getVarInt64())
        continue
      if tt == 138:
        self.set_name(d.getPrefixedString())
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_type_: res+=prefix+("type: %s\n" % self.DebugFormatString(self.type_))
    if self.has_id_: res+=prefix+("id: %s\n" % self.DebugFormatInt64(self.id_))
    if self.has_name_: res+=prefix+("name: %s\n" % self.DebugFormatString(self.name_))
    return res

class PropertyValue_PointValue(ProtocolBuffer.ProtocolMessage):
  has_x_ = 0
  x_ = 0.0
  has_y_ = 0
  y_ = 0.0

  def __init__(self, contents=None):
    if contents is not None: self.MergeFromString(contents)

  def x(self): return self.x_

  def set_x(self, x):
    self.has_x_ = 1
    self.x_ = x

  def clear_x(self):
    self.has_x_ = 0
    self.x_ = 0.0

  def has_x(self): return self.has_x_

  def y(self): return self.y_

  def set_y(self, x):
    self.has_y_ = 1
    self.y_ = x

  def clear_y(self):
    self.has_y_ = 0
    self.y_ = 0.0

  def has_y(self): return self.has_y_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_x()): self.set_x(x.x())
    if (x.has_y()): self.set_y(x.y())

  def Equals(self, x):
    if x is self: return 1
    if self.has_x_ != x.has_x_: return 0
    if self.has_x_ and self.x_ != x.x_: return 0
    if self.has_y_ != x.has_y_: return 0
    if self.has_y_ and self.y_ != x.y_: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_x_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: x not set.')
    if (not self.has_y_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: y not set.')
    return initialized

  def ByteSize(self):
    n = 0
    return n + 18

  def Clear(self):
    self.clear_x()
    self.clear_y()

  def OutputUnchecked(self, out):
    out.putVarInt32(49)
    out.putDouble(self.x_)
    out.putVarInt32(57)
    out.putDouble(self.y_)

  def TryMerge(self, d):
    while 1:
      tt = d.getVarInt32()
      if tt == 44: break
      if tt == 49:
        self.set_x(d.getDouble())
        continue
      if tt == 57:
        self.set_y(d.getDouble())
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_x_: res+=prefix+("x: %s\n" % self.DebugFormat(self.x_))
    if self.has_y_: res+=prefix+("y: %s\n" % self.DebugFormat(self.y_))
    return res

class PropertyValue_UserValue(ProtocolBuffer.ProtocolMessage):
  has_email_ = 0
  email_ = ""
  has_auth_domain_ = 0
  auth_domain_ = ""
  has_nickname_ = 0
  nickname_ = ""
  has_gaiaid_ = 0
  gaiaid_ = 0

  def __init__(self, contents=None):
    if contents is not None: self.MergeFromString(contents)

  def email(self): return self.email_

  def set_email(self, x):
    self.has_email_ = 1
    self.email_ = x

  def clear_email(self):
    self.has_email_ = 0
    self.email_ = ""

  def has_email(self): return self.has_email_

  def auth_domain(self): return self.auth_domain_

  def set_auth_domain(self, x):
    self.has_auth_domain_ = 1
    self.auth_domain_ = x

  def clear_auth_domain(self):
    self.has_auth_domain_ = 0
    self.auth_domain_ = ""

  def has_auth_domain(self): return self.has_auth_domain_

  def nickname(self): return self.nickname_

  def set_nickname(self, x):
    self.has_nickname_ = 1
    self.nickname_ = x

  def clear_nickname(self):
    self.has_nickname_ = 0
    self.nickname_ = ""

  def has_nickname(self): return self.has_nickname_

  def gaiaid(self): return self.gaiaid_

  def set_gaiaid(self, x):
    self.has_gaiaid_ = 1
    self.gaiaid_ = x

  def clear_gaiaid(self):
    self.has_gaiaid_ = 0
    self.gaiaid_ = 0

  def has_gaiaid(self): return self.has_gaiaid_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_email()): self.set_email(x.email())
    if (x.has_auth_domain()): self.set_auth_domain(x.auth_domain())
    if (x.has_nickname()): self.set_nickname(x.nickname())
    if (x.has_gaiaid()): self.set_gaiaid(x.gaiaid())

  def Equals(self, x):
    if x is self: return 1
    if self.has_email_ != x.has_email_: return 0
    if self.has_email_ and self.email_ != x.email_: return 0
    if self.has_auth_domain_ != x.has_auth_domain_: return 0
    if self.has_auth_domain_ and self.auth_domain_ != x.auth_domain_: return 0
    if self.has_nickname_ != x.has_nickname_: return 0
    if self.has_nickname_ and self.nickname_ != x.nickname_: return 0
    if self.has_gaiaid_ != x.has_gaiaid_: return 0
    if self.has_gaiaid_ and self.gaiaid_ != x.gaiaid_: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_email_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: email not set.')
    if (not self.has_auth_domain_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: auth_domain not set.')
    if (not self.has_gaiaid_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: gaiaid not set.')
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthString(len(self.email_))
    n += self.lengthString(len(self.auth_domain_))
    if (self.has_nickname_): n += 1 + self.lengthString(len(self.nickname_))
    n += self.lengthVarInt64(self.gaiaid_)
    return n + 4

  def Clear(self):
    self.clear_email()
    self.clear_auth_domain()
    self.clear_nickname()
    self.clear_gaiaid()

  def OutputUnchecked(self, out):
    out.putVarInt32(74)
    out.putPrefixedString(self.email_)
    out.putVarInt32(82)
    out.putPrefixedString(self.auth_domain_)
    if (self.has_nickname_):
      out.putVarInt32(90)
      out.putPrefixedString(self.nickname_)
    out.putVarInt32(144)
    out.putVarInt64(self.gaiaid_)

  def TryMerge(self, d):
    while 1:
      tt = d.getVarInt32()
      if tt == 68: break
      if tt == 74:
        self.set_email(d.getPrefixedString())
        continue
      if tt == 82:
        self.set_auth_domain(d.getPrefixedString())
        continue
      if tt == 90:
        self.set_nickname(d.getPrefixedString())
        continue
      if tt == 144:
        self.set_gaiaid(d.getVarInt64())
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_email_: res+=prefix+("email: %s\n" % self.DebugFormatString(self.email_))
    if self.has_auth_domain_: res+=prefix+("auth_domain: %s\n" % self.DebugFormatString(self.auth_domain_))
    if self.has_nickname_: res+=prefix+("nickname: %s\n" % self.DebugFormatString(self.nickname_))
    if self.has_gaiaid_: res+=prefix+("gaiaid: %s\n" % self.DebugFormatInt64(self.gaiaid_))
    return res

class PropertyValue_ReferenceValue(ProtocolBuffer.ProtocolMessage):
  has_app_ = 0
  app_ = ""

  def __init__(self, contents=None):
    self.pathelement_ = []
    if contents is not None: self.MergeFromString(contents)

  def app(self): return self.app_

  def set_app(self, x):
    self.has_app_ = 1
    self.app_ = x

  def clear_app(self):
    self.has_app_ = 0
    self.app_ = ""

  def has_app(self): return self.has_app_

  def pathelement_size(self): return len(self.pathelement_)
  def pathelement_list(self): return self.pathelement_

  def pathelement(self, i):
    return self.pathelement_[i]

  def mutable_pathelement(self, i):
    return self.pathelement_[i]

  def add_pathelement(self):
    x = PropertyValue_ReferenceValuePathElement()
    self.pathelement_.append(x)
    return x

  def clear_pathelement(self):
    self.pathelement_ = []

  def MergeFrom(self, x):
    assert x is not self
    if (x.has_app()): self.set_app(x.app())
    for i in xrange(x.pathelement_size()): self.add_pathelement().CopyFrom(x.pathelement(i))

  def Equals(self, x):
    if x is self: return 1
    if self.has_app_ != x.has_app_: return 0
    if self.has_app_ and self.app_ != x.app_: return 0
    if len(self.pathelement_) != len(x.pathelement_): return 0
    for e1, e2 in zip(self.pathelement_, x.pathelement_):
      if e1 != e2: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_app_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: app not set.')
    for p in self.pathelement_:
      if not p.IsInitialized(debug_strs): initialized=0
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthString(len(self.app_))
    n += 2 * len(self.pathelement_)
    for i in xrange(len(self.pathelement_)): n += self.pathelement_[i].ByteSize()
    return n + 1

  def Clear(self):
    self.clear_app()
    self.clear_pathelement()

  def OutputUnchecked(self, out):
    out.putVarInt32(106)
    out.putPrefixedString(self.app_)
    for i in xrange(len(self.pathelement_)):
      out.putVarInt32(115)
      self.pathelement_[i].OutputUnchecked(out)
      out.putVarInt32(116)

  def TryMerge(self, d):
    while 1:
      tt = d.getVarInt32()
      if tt == 100: break
      if tt == 106:
        self.set_app(d.getPrefixedString())
        continue
      if tt == 115:
        self.add_pathelement().TryMerge(d)
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_app_: res+=prefix+("app: %s\n" % self.DebugFormatString(self.app_))
    cnt=0
    for e in self.pathelement_:
      elm=""
      if printElemNumber: elm="(%d)" % cnt
      res+=prefix+("PathElement%s {\n" % elm)
      res+=e.__str__(prefix + "  ", printElemNumber)
      res+=prefix+"}\n"
      cnt+=1
    return res

class PropertyValue(ProtocolBuffer.ProtocolMessage):
  has_int64value_ = 0
  int64value_ = 0
  has_booleanvalue_ = 0
  booleanvalue_ = 0
  has_stringvalue_ = 0
  stringvalue_ = ""
  has_doublevalue_ = 0
  doublevalue_ = 0.0
  has_pointvalue_ = 0
  pointvalue_ = None
  has_uservalue_ = 0
  uservalue_ = None
  has_referencevalue_ = 0
  referencevalue_ = None

  def __init__(self, contents=None):
    self.lazy_init_lock_ = thread.allocate_lock()
    if contents is not None: self.MergeFromString(contents)

  def int64value(self): return self.int64value_

  def set_int64value(self, x):
    self.has_int64value_ = 1
    self.int64value_ = x

  def clear_int64value(self):
    self.has_int64value_ = 0
    self.int64value_ = 0

  def has_int64value(self): return self.has_int64value_

  def booleanvalue(self): return self.booleanvalue_

  def set_booleanvalue(self, x):
    self.has_booleanvalue_ = 1
    self.booleanvalue_ = x

  def clear_booleanvalue(self):
    self.has_booleanvalue_ = 0
    self.booleanvalue_ = 0

  def has_booleanvalue(self): return self.has_booleanvalue_

  def stringvalue(self): return self.stringvalue_

  def set_stringvalue(self, x):
    self.has_stringvalue_ = 1
    self.stringvalue_ = x

  def clear_stringvalue(self):
    self.has_stringvalue_ = 0
    self.stringvalue_ = ""

  def has_stringvalue(self): return self.has_stringvalue_

  def doublevalue(self): return self.doublevalue_

  def set_doublevalue(self, x):
    self.has_doublevalue_ = 1
    self.doublevalue_ = x

  def clear_doublevalue(self):
    self.has_doublevalue_ = 0
    self.doublevalue_ = 0.0

  def has_doublevalue(self): return self.has_doublevalue_

  def pointvalue(self):
    if self.pointvalue_ is None:
      self.lazy_init_lock_.acquire()
      try:
        if self.pointvalue_ is None: self.pointvalue_ = PropertyValue_PointValue()
      finally:
        self.lazy_init_lock_.release()
    return self.pointvalue_

  def mutable_pointvalue(self): self.has_pointvalue_ = 1; return self.pointvalue()

  def clear_pointvalue(self):
    self.has_pointvalue_ = 0;
    if self.pointvalue_ is not None: self.pointvalue_.Clear()

  def has_pointvalue(self): return self.has_pointvalue_

  def uservalue(self):
    if self.uservalue_ is None:
      self.lazy_init_lock_.acquire()
      try:
        if self.uservalue_ is None: self.uservalue_ = PropertyValue_UserValue()
      finally:
        self.lazy_init_lock_.release()
    return self.uservalue_

  def mutable_uservalue(self): self.has_uservalue_ = 1; return self.uservalue()

  def clear_uservalue(self):
    self.has_uservalue_ = 0;
    if self.uservalue_ is not None: self.uservalue_.Clear()

  def has_uservalue(self): return self.has_uservalue_

  def referencevalue(self):
    if self.referencevalue_ is None:
      self.lazy_init_lock_.acquire()
      try:
        if self.referencevalue_ is None: self.referencevalue_ = PropertyValue_ReferenceValue()
      finally:
        self.lazy_init_lock_.release()
    return self.referencevalue_

  def mutable_referencevalue(self): self.has_referencevalue_ = 1; return self.referencevalue()

  def clear_referencevalue(self):
    self.has_referencevalue_ = 0;
    if self.referencevalue_ is not None: self.referencevalue_.Clear()

  def has_referencevalue(self): return self.has_referencevalue_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_int64value()): self.set_int64value(x.int64value())
    if (x.has_booleanvalue()): self.set_booleanvalue(x.booleanvalue())
    if (x.has_stringvalue()): self.set_stringvalue(x.stringvalue())
    if (x.has_doublevalue()): self.set_doublevalue(x.doublevalue())
    if (x.has_pointvalue()): self.mutable_pointvalue().MergeFrom(x.pointvalue())
    if (x.has_uservalue()): self.mutable_uservalue().MergeFrom(x.uservalue())
    if (x.has_referencevalue()): self.mutable_referencevalue().MergeFrom(x.referencevalue())

  def Equals(self, x):
    if x is self: return 1
    if self.has_int64value_ != x.has_int64value_: return 0
    if self.has_int64value_ and self.int64value_ != x.int64value_: return 0
    if self.has_booleanvalue_ != x.has_booleanvalue_: return 0
    if self.has_booleanvalue_ and self.booleanvalue_ != x.booleanvalue_: return 0
    if self.has_stringvalue_ != x.has_stringvalue_: return 0
    if self.has_stringvalue_ and self.stringvalue_ != x.stringvalue_: return 0
    if self.has_doublevalue_ != x.has_doublevalue_: return 0
    if self.has_doublevalue_ and self.doublevalue_ != x.doublevalue_: return 0
    if self.has_pointvalue_ != x.has_pointvalue_: return 0
    if self.has_pointvalue_ and self.pointvalue_ != x.pointvalue_: return 0
    if self.has_uservalue_ != x.has_uservalue_: return 0
    if self.has_uservalue_ and self.uservalue_ != x.uservalue_: return 0
    if self.has_referencevalue_ != x.has_referencevalue_: return 0
    if self.has_referencevalue_ and self.referencevalue_ != x.referencevalue_: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (self.has_pointvalue_ and not self.pointvalue_.IsInitialized(debug_strs)): initialized = 0
    if (self.has_uservalue_ and not self.uservalue_.IsInitialized(debug_strs)): initialized = 0
    if (self.has_referencevalue_ and not self.referencevalue_.IsInitialized(debug_strs)): initialized = 0
    return initialized

  def ByteSize(self):
    n = 0
    if (self.has_int64value_): n += 1 + self.lengthVarInt64(self.int64value_)
    if (self.has_booleanvalue_): n += 2
    if (self.has_stringvalue_): n += 1 + self.lengthString(len(self.stringvalue_))
    if (self.has_doublevalue_): n += 9
    if (self.has_pointvalue_): n += 2 + self.pointvalue_.ByteSize()
    if (self.has_uservalue_): n += 2 + self.uservalue_.ByteSize()
    if (self.has_referencevalue_): n += 2 + self.referencevalue_.ByteSize()
    return n + 0

  def Clear(self):
    self.clear_int64value()
    self.clear_booleanvalue()
    self.clear_stringvalue()
    self.clear_doublevalue()
    self.clear_pointvalue()
    self.clear_uservalue()
    self.clear_referencevalue()

  def OutputUnchecked(self, out):
    if (self.has_int64value_):
      out.putVarInt32(8)
      out.putVarInt64(self.int64value_)
    if (self.has_booleanvalue_):
      out.putVarInt32(16)
      out.putBoolean(self.booleanvalue_)
    if (self.has_stringvalue_):
      out.putVarInt32(26)
      out.putPrefixedString(self.stringvalue_)
    if (self.has_doublevalue_):
      out.putVarInt32(33)
      out.putDouble(self.doublevalue_)
    if (self.has_pointvalue_):
      out.putVarInt32(43)
      self.pointvalue_.OutputUnchecked(out)
      out.putVarInt32(44)
    if (self.has_uservalue_):
      out.putVarInt32(67)
      self.uservalue_.OutputUnchecked(out)
      out.putVarInt32(68)
    if (self.has_referencevalue_):
      out.putVarInt32(99)
      self.referencevalue_.OutputUnchecked(out)
      out.putVarInt32(100)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 8:
        self.set_int64value(d.getVarInt64())
        continue
      if tt == 16:
        self.set_booleanvalue(d.getBoolean())
        continue
      if tt == 26:
        self.set_stringvalue(d.getPrefixedString())
        continue
      if tt == 33:
        self.set_doublevalue(d.getDouble())
        continue
      if tt == 43:
        self.mutable_pointvalue().TryMerge(d)
        continue
      if tt == 67:
        self.mutable_uservalue().TryMerge(d)
        continue
      if tt == 99:
        self.mutable_referencevalue().TryMerge(d)
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_int64value_: res+=prefix+("int64Value: %s\n" % self.DebugFormatInt64(self.int64value_))
    if self.has_booleanvalue_: res+=prefix+("booleanValue: %s\n" % self.DebugFormatBool(self.booleanvalue_))
    if self.has_stringvalue_: res+=prefix+("stringValue: %s\n" % self.DebugFormatString(self.stringvalue_))
    if self.has_doublevalue_: res+=prefix+("doubleValue: %s\n" % self.DebugFormat(self.doublevalue_))
    if self.has_pointvalue_:
      res+=prefix+"PointValue {\n"
      res+=self.pointvalue_.__str__(prefix + "  ", printElemNumber)
      res+=prefix+"}\n"
    if self.has_uservalue_:
      res+=prefix+"UserValue {\n"
      res+=self.uservalue_.__str__(prefix + "  ", printElemNumber)
      res+=prefix+"}\n"
    if self.has_referencevalue_:
      res+=prefix+"ReferenceValue {\n"
      res+=self.referencevalue_.__str__(prefix + "  ", printElemNumber)
      res+=prefix+"}\n"
    return res

  kint64Value = 1
  kbooleanValue = 2
  kstringValue = 3
  kdoubleValue = 4
  kPointValueGroup = 5
  kPointValuex = 6
  kPointValuey = 7
  kUserValueGroup = 8
  kUserValueemail = 9
  kUserValueauth_domain = 10
  kUserValuenickname = 11
  kUserValuegaiaid = 18
  kReferenceValueGroup = 12
  kReferenceValueapp = 13
  kReferenceValuePathElementGroup = 14
  kReferenceValuePathElementtype = 15
  kReferenceValuePathElementid = 16
  kReferenceValuePathElementname = 17

  _TEXT = (
   "ErrorCode",
   "int64Value",
   "booleanValue",
   "stringValue",
   "doubleValue",
   "PointValue",
   "x",
   "y",
   "UserValue",
   "email",
   "auth_domain",
   "nickname",
   "ReferenceValue",
   "app",
   "PathElement",
   "type",
   "id",
   "name",
   "gaiaid",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
   ProtocolBuffer.Encoder.NUMERIC,

   ProtocolBuffer.Encoder.NUMERIC,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.DOUBLE,

   ProtocolBuffer.Encoder.STARTGROUP,

   ProtocolBuffer.Encoder.DOUBLE,

   ProtocolBuffer.Encoder.DOUBLE,

   ProtocolBuffer.Encoder.STARTGROUP,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.STARTGROUP,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.STARTGROUP,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.NUMERIC,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.NUMERIC,

  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class Property(ProtocolBuffer.ProtocolMessage):

  BLOB         =   14
  TEXT         =   15
  ATOM_CATEGORY =    1
  ATOM_LINK    =    2
  ATOM_TITLE   =    3
  ATOM_CONTENT =    4
  ATOM_SUMMARY =    5
  ATOM_AUTHOR  =    6
  GD_WHEN      =    7
  GD_EMAIL     =    8
  GEORSS_POINT =    9
  GD_IM        =   10
  GD_PHONENUMBER =   11
  GD_POSTALADDRESS =   12
  GD_RATING    =   13

  _Meaning_NAMES = {
    14: "BLOB",
    15: "TEXT",
    1: "ATOM_CATEGORY",
    2: "ATOM_LINK",
    3: "ATOM_TITLE",
    4: "ATOM_CONTENT",
    5: "ATOM_SUMMARY",
    6: "ATOM_AUTHOR",
    7: "GD_WHEN",
    8: "GD_EMAIL",
    9: "GEORSS_POINT",
    10: "GD_IM",
    11: "GD_PHONENUMBER",
    12: "GD_POSTALADDRESS",
    13: "GD_RATING",
  }

  def Meaning_Name(cls, x): return cls._Meaning_NAMES.get(x, "")
  Meaning_Name = classmethod(Meaning_Name)

  has_meaning_ = 0
  meaning_ = 0
  has_meaning_uri_ = 0
  meaning_uri_ = ""
  has_name_ = 0
  name_ = ""
  has_value_ = 0
  has_multiple_ = 0
  multiple_ = 0

  def __init__(self, contents=None):
    self.value_ = PropertyValue()
    if contents is not None: self.MergeFromString(contents)

  def meaning(self): return self.meaning_

  def set_meaning(self, x):
    self.has_meaning_ = 1
    self.meaning_ = x

  def clear_meaning(self):
    self.has_meaning_ = 0
    self.meaning_ = 0

  def has_meaning(self): return self.has_meaning_

  def meaning_uri(self): return self.meaning_uri_

  def set_meaning_uri(self, x):
    self.has_meaning_uri_ = 1
    self.meaning_uri_ = x

  def clear_meaning_uri(self):
    self.has_meaning_uri_ = 0
    self.meaning_uri_ = ""

  def has_meaning_uri(self): return self.has_meaning_uri_

  def name(self): return self.name_

  def set_name(self, x):
    self.has_name_ = 1
    self.name_ = x

  def clear_name(self):
    self.has_name_ = 0
    self.name_ = ""

  def has_name(self): return self.has_name_

  def value(self): return self.value_

  def mutable_value(self): self.has_value_ = 1; return self.value_

  def clear_value(self):self.has_value_ = 0; self.value_.Clear()

  def has_value(self): return self.has_value_

  def multiple(self): return self.multiple_

  def set_multiple(self, x):
    self.has_multiple_ = 1
    self.multiple_ = x

  def clear_multiple(self):
    self.has_multiple_ = 0
    self.multiple_ = 0

  def has_multiple(self): return self.has_multiple_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_meaning()): self.set_meaning(x.meaning())
    if (x.has_meaning_uri()): self.set_meaning_uri(x.meaning_uri())
    if (x.has_name()): self.set_name(x.name())
    if (x.has_value()): self.mutable_value().MergeFrom(x.value())
    if (x.has_multiple()): self.set_multiple(x.multiple())

  def Equals(self, x):
    if x is self: return 1
    if self.has_meaning_ != x.has_meaning_: return 0
    if self.has_meaning_ and self.meaning_ != x.meaning_: return 0
    if self.has_meaning_uri_ != x.has_meaning_uri_: return 0
    if self.has_meaning_uri_ and self.meaning_uri_ != x.meaning_uri_: return 0
    if self.has_name_ != x.has_name_: return 0
    if self.has_name_ and self.name_ != x.name_: return 0
    if self.has_value_ != x.has_value_: return 0
    if self.has_value_ and self.value_ != x.value_: return 0
    if self.has_multiple_ != x.has_multiple_: return 0
    if self.has_multiple_ and self.multiple_ != x.multiple_: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_name_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: name not set.')
    if (not self.has_value_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: value not set.')
    elif not self.value_.IsInitialized(debug_strs): initialized = 0
    return initialized

  def ByteSize(self):
    n = 0
    if (self.has_meaning_): n += 1 + self.lengthVarInt64(self.meaning_)
    if (self.has_meaning_uri_): n += 1 + self.lengthString(len(self.meaning_uri_))
    n += self.lengthString(len(self.name_))
    n += self.lengthString(self.value_.ByteSize())
    if (self.has_multiple_): n += 2
    return n + 2

  def Clear(self):
    self.clear_meaning()
    self.clear_meaning_uri()
    self.clear_name()
    self.clear_value()
    self.clear_multiple()

  def OutputUnchecked(self, out):
    if (self.has_meaning_):
      out.putVarInt32(8)
      out.putVarInt32(self.meaning_)
    if (self.has_meaning_uri_):
      out.putVarInt32(18)
      out.putPrefixedString(self.meaning_uri_)
    out.putVarInt32(26)
    out.putPrefixedString(self.name_)
    if (self.has_multiple_):
      out.putVarInt32(32)
      out.putBoolean(self.multiple_)
    out.putVarInt32(42)
    out.putVarInt32(self.value_.ByteSize())
    self.value_.OutputUnchecked(out)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 8:
        self.set_meaning(d.getVarInt32())
        continue
      if tt == 18:
        self.set_meaning_uri(d.getPrefixedString())
        continue
      if tt == 26:
        self.set_name(d.getPrefixedString())
        continue
      if tt == 32:
        self.set_multiple(d.getBoolean())
        continue
      if tt == 42:
        length = d.getVarInt32()
        tmp = ProtocolBuffer.Decoder(d.buffer(), d.pos(), d.pos() + length)
        d.skip(length)
        self.mutable_value().TryMerge(tmp)
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_meaning_: res+=prefix+("meaning: %s\n" % self.DebugFormatInt32(self.meaning_))
    if self.has_meaning_uri_: res+=prefix+("meaning_uri: %s\n" % self.DebugFormatString(self.meaning_uri_))
    if self.has_name_: res+=prefix+("name: %s\n" % self.DebugFormatString(self.name_))
    if self.has_value_:
      res+=prefix+"value <\n"
      res+=self.value_.__str__(prefix + "  ", printElemNumber)
      res+=prefix+">\n"
    if self.has_multiple_: res+=prefix+("multiple: %s\n" % self.DebugFormatBool(self.multiple_))
    return res

  kmeaning = 1
  kmeaning_uri = 2
  kname = 3
  kvalue = 5
  kmultiple = 4

  _TEXT = (
   "ErrorCode",
   "meaning",
   "meaning_uri",
   "name",
   "multiple",
   "value",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
   ProtocolBuffer.Encoder.NUMERIC,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.NUMERIC,

   ProtocolBuffer.Encoder.STRING,

  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class Path_Element(ProtocolBuffer.ProtocolMessage):
  has_type_ = 0
  type_ = ""
  has_id_ = 0
  id_ = 0
  has_name_ = 0
  name_ = ""

  def __init__(self, contents=None):
    if contents is not None: self.MergeFromString(contents)

  def type(self): return self.type_

  def set_type(self, x):
    self.has_type_ = 1
    self.type_ = x

  def clear_type(self):
    self.has_type_ = 0
    self.type_ = ""

  def has_type(self): return self.has_type_

  def id(self): return self.id_

  def set_id(self, x):
    self.has_id_ = 1
    self.id_ = x

  def clear_id(self):
    self.has_id_ = 0
    self.id_ = 0

  def has_id(self): return self.has_id_

  def name(self): return self.name_

  def set_name(self, x):
    self.has_name_ = 1
    self.name_ = x

  def clear_name(self):
    self.has_name_ = 0
    self.name_ = ""

  def has_name(self): return self.has_name_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_type()): self.set_type(x.type())
    if (x.has_id()): self.set_id(x.id())
    if (x.has_name()): self.set_name(x.name())

  def Equals(self, x):
    if x is self: return 1
    if self.has_type_ != x.has_type_: return 0
    if self.has_type_ and self.type_ != x.type_: return 0
    if self.has_id_ != x.has_id_: return 0
    if self.has_id_ and self.id_ != x.id_: return 0
    if self.has_name_ != x.has_name_: return 0
    if self.has_name_ and self.name_ != x.name_: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_type_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: type not set.')
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthString(len(self.type_))
    if (self.has_id_): n += 1 + self.lengthVarInt64(self.id_)
    if (self.has_name_): n += 1 + self.lengthString(len(self.name_))
    return n + 1

  def Clear(self):
    self.clear_type()
    self.clear_id()
    self.clear_name()

  def OutputUnchecked(self, out):
    out.putVarInt32(18)
    out.putPrefixedString(self.type_)
    if (self.has_id_):
      out.putVarInt32(24)
      out.putVarInt64(self.id_)
    if (self.has_name_):
      out.putVarInt32(34)
      out.putPrefixedString(self.name_)

  def TryMerge(self, d):
    while 1:
      tt = d.getVarInt32()
      if tt == 12: break
      if tt == 18:
        self.set_type(d.getPrefixedString())
        continue
      if tt == 24:
        self.set_id(d.getVarInt64())
        continue
      if tt == 34:
        self.set_name(d.getPrefixedString())
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_type_: res+=prefix+("type: %s\n" % self.DebugFormatString(self.type_))
    if self.has_id_: res+=prefix+("id: %s\n" % self.DebugFormatInt64(self.id_))
    if self.has_name_: res+=prefix+("name: %s\n" % self.DebugFormatString(self.name_))
    return res

class Path(ProtocolBuffer.ProtocolMessage):

  def __init__(self, contents=None):
    self.element_ = []
    if contents is not None: self.MergeFromString(contents)

  def element_size(self): return len(self.element_)
  def element_list(self): return self.element_

  def element(self, i):
    return self.element_[i]

  def mutable_element(self, i):
    return self.element_[i]

  def add_element(self):
    x = Path_Element()
    self.element_.append(x)
    return x

  def clear_element(self):
    self.element_ = []

  def MergeFrom(self, x):
    assert x is not self
    for i in xrange(x.element_size()): self.add_element().CopyFrom(x.element(i))

  def Equals(self, x):
    if x is self: return 1
    if len(self.element_) != len(x.element_): return 0
    for e1, e2 in zip(self.element_, x.element_):
      if e1 != e2: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    for p in self.element_:
      if not p.IsInitialized(debug_strs): initialized=0
    return initialized

  def ByteSize(self):
    n = 0
    n += 2 * len(self.element_)
    for i in xrange(len(self.element_)): n += self.element_[i].ByteSize()
    return n + 0

  def Clear(self):
    self.clear_element()

  def OutputUnchecked(self, out):
    for i in xrange(len(self.element_)):
      out.putVarInt32(11)
      self.element_[i].OutputUnchecked(out)
      out.putVarInt32(12)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 11:
        self.add_element().TryMerge(d)
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    cnt=0
    for e in self.element_:
      elm=""
      if printElemNumber: elm="(%d)" % cnt
      res+=prefix+("Element%s {\n" % elm)
      res+=e.__str__(prefix + "  ", printElemNumber)
      res+=prefix+"}\n"
      cnt+=1
    return res

  kElementGroup = 1
  kElementtype = 2
  kElementid = 3
  kElementname = 4

  _TEXT = (
   "ErrorCode",
   "Element",
   "type",
   "id",
   "name",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
   ProtocolBuffer.Encoder.STARTGROUP,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.NUMERIC,

   ProtocolBuffer.Encoder.STRING,

  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class Reference(ProtocolBuffer.ProtocolMessage):
  has_app_ = 0
  app_ = ""
  has_path_ = 0

  def __init__(self, contents=None):
    self.path_ = Path()
    if contents is not None: self.MergeFromString(contents)

  def app(self): return self.app_

  def set_app(self, x):
    self.has_app_ = 1
    self.app_ = x

  def clear_app(self):
    self.has_app_ = 0
    self.app_ = ""

  def has_app(self): return self.has_app_

  def path(self): return self.path_

  def mutable_path(self): self.has_path_ = 1; return self.path_

  def clear_path(self):self.has_path_ = 0; self.path_.Clear()

  def has_path(self): return self.has_path_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_app()): self.set_app(x.app())
    if (x.has_path()): self.mutable_path().MergeFrom(x.path())

  def Equals(self, x):
    if x is self: return 1
    if self.has_app_ != x.has_app_: return 0
    if self.has_app_ and self.app_ != x.app_: return 0
    if self.has_path_ != x.has_path_: return 0
    if self.has_path_ and self.path_ != x.path_: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_app_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: app not set.')
    if (not self.has_path_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: path not set.')
    elif not self.path_.IsInitialized(debug_strs): initialized = 0
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthString(len(self.app_))
    n += self.lengthString(self.path_.ByteSize())
    return n + 2

  def Clear(self):
    self.clear_app()
    self.clear_path()

  def OutputUnchecked(self, out):
    out.putVarInt32(106)
    out.putPrefixedString(self.app_)
    out.putVarInt32(114)
    out.putVarInt32(self.path_.ByteSize())
    self.path_.OutputUnchecked(out)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 106:
        self.set_app(d.getPrefixedString())
        continue
      if tt == 114:
        length = d.getVarInt32()
        tmp = ProtocolBuffer.Decoder(d.buffer(), d.pos(), d.pos() + length)
        d.skip(length)
        self.mutable_path().TryMerge(tmp)
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_app_: res+=prefix+("app: %s\n" % self.DebugFormatString(self.app_))
    if self.has_path_:
      res+=prefix+"path <\n"
      res+=self.path_.__str__(prefix + "  ", printElemNumber)
      res+=prefix+">\n"
    return res

  kapp = 13
  kpath = 14

  _TEXT = (
   "ErrorCode",
   None,
   None,
   None,
   None,
   None,
   None,
   None,
   None,
   None,
   None,
   None,
   None,
   "app",
   "path",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
   ProtocolBuffer.Encoder.MAX_TYPE,

   ProtocolBuffer.Encoder.MAX_TYPE,

   ProtocolBuffer.Encoder.MAX_TYPE,

   ProtocolBuffer.Encoder.MAX_TYPE,

   ProtocolBuffer.Encoder.MAX_TYPE,

   ProtocolBuffer.Encoder.MAX_TYPE,

   ProtocolBuffer.Encoder.MAX_TYPE,

   ProtocolBuffer.Encoder.MAX_TYPE,

   ProtocolBuffer.Encoder.MAX_TYPE,

   ProtocolBuffer.Encoder.MAX_TYPE,

   ProtocolBuffer.Encoder.MAX_TYPE,

   ProtocolBuffer.Encoder.MAX_TYPE,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.STRING,

  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class User(ProtocolBuffer.ProtocolMessage):
  has_email_ = 0
  email_ = ""
  has_auth_domain_ = 0
  auth_domain_ = ""
  has_nickname_ = 0
  nickname_ = ""
  has_gaiaid_ = 0
  gaiaid_ = 0

  def __init__(self, contents=None):
    if contents is not None: self.MergeFromString(contents)

  def email(self): return self.email_

  def set_email(self, x):
    self.has_email_ = 1
    self.email_ = x

  def clear_email(self):
    self.has_email_ = 0
    self.email_ = ""

  def has_email(self): return self.has_email_

  def auth_domain(self): return self.auth_domain_

  def set_auth_domain(self, x):
    self.has_auth_domain_ = 1
    self.auth_domain_ = x

  def clear_auth_domain(self):
    self.has_auth_domain_ = 0
    self.auth_domain_ = ""

  def has_auth_domain(self): return self.has_auth_domain_

  def nickname(self): return self.nickname_

  def set_nickname(self, x):
    self.has_nickname_ = 1
    self.nickname_ = x

  def clear_nickname(self):
    self.has_nickname_ = 0
    self.nickname_ = ""

  def has_nickname(self): return self.has_nickname_

  def gaiaid(self): return self.gaiaid_

  def set_gaiaid(self, x):
    self.has_gaiaid_ = 1
    self.gaiaid_ = x

  def clear_gaiaid(self):
    self.has_gaiaid_ = 0
    self.gaiaid_ = 0

  def has_gaiaid(self): return self.has_gaiaid_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_email()): self.set_email(x.email())
    if (x.has_auth_domain()): self.set_auth_domain(x.auth_domain())
    if (x.has_nickname()): self.set_nickname(x.nickname())
    if (x.has_gaiaid()): self.set_gaiaid(x.gaiaid())

  def Equals(self, x):
    if x is self: return 1
    if self.has_email_ != x.has_email_: return 0
    if self.has_email_ and self.email_ != x.email_: return 0
    if self.has_auth_domain_ != x.has_auth_domain_: return 0
    if self.has_auth_domain_ and self.auth_domain_ != x.auth_domain_: return 0
    if self.has_nickname_ != x.has_nickname_: return 0
    if self.has_nickname_ and self.nickname_ != x.nickname_: return 0
    if self.has_gaiaid_ != x.has_gaiaid_: return 0
    if self.has_gaiaid_ and self.gaiaid_ != x.gaiaid_: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_email_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: email not set.')
    if (not self.has_auth_domain_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: auth_domain not set.')
    if (not self.has_gaiaid_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: gaiaid not set.')
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthString(len(self.email_))
    n += self.lengthString(len(self.auth_domain_))
    if (self.has_nickname_): n += 1 + self.lengthString(len(self.nickname_))
    n += self.lengthVarInt64(self.gaiaid_)
    return n + 3

  def Clear(self):
    self.clear_email()
    self.clear_auth_domain()
    self.clear_nickname()
    self.clear_gaiaid()

  def OutputUnchecked(self, out):
    out.putVarInt32(10)
    out.putPrefixedString(self.email_)
    out.putVarInt32(18)
    out.putPrefixedString(self.auth_domain_)
    if (self.has_nickname_):
      out.putVarInt32(26)
      out.putPrefixedString(self.nickname_)
    out.putVarInt32(32)
    out.putVarInt64(self.gaiaid_)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 10:
        self.set_email(d.getPrefixedString())
        continue
      if tt == 18:
        self.set_auth_domain(d.getPrefixedString())
        continue
      if tt == 26:
        self.set_nickname(d.getPrefixedString())
        continue
      if tt == 32:
        self.set_gaiaid(d.getVarInt64())
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_email_: res+=prefix+("email: %s\n" % self.DebugFormatString(self.email_))
    if self.has_auth_domain_: res+=prefix+("auth_domain: %s\n" % self.DebugFormatString(self.auth_domain_))
    if self.has_nickname_: res+=prefix+("nickname: %s\n" % self.DebugFormatString(self.nickname_))
    if self.has_gaiaid_: res+=prefix+("gaiaid: %s\n" % self.DebugFormatInt64(self.gaiaid_))
    return res

  kemail = 1
  kauth_domain = 2
  knickname = 3
  kgaiaid = 4

  _TEXT = (
   "ErrorCode",
   "email",
   "auth_domain",
   "nickname",
   "gaiaid",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.NUMERIC,

  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class EntityProto(ProtocolBuffer.ProtocolMessage):

  GD_CONTACT   =    1
  GD_EVENT     =    2
  GD_MESSAGE   =    3

  _Kind_NAMES = {
    1: "GD_CONTACT",
    2: "GD_EVENT",
    3: "GD_MESSAGE",
  }

  def Kind_Name(cls, x): return cls._Kind_NAMES.get(x, "")
  Kind_Name = classmethod(Kind_Name)

  has_key_ = 0
  has_entity_group_ = 0
  has_owner_ = 0
  owner_ = None
  has_kind_ = 0
  kind_ = 0
  has_kind_uri_ = 0
  kind_uri_ = ""

  def __init__(self, contents=None):
    self.key_ = Reference()
    self.entity_group_ = Path()
    self.property_ = []
    self.raw_property_ = []
    self.lazy_init_lock_ = thread.allocate_lock()
    if contents is not None: self.MergeFromString(contents)

  def key(self): return self.key_

  def mutable_key(self): self.has_key_ = 1; return self.key_

  def clear_key(self):self.has_key_ = 0; self.key_.Clear()

  def has_key(self): return self.has_key_

  def entity_group(self): return self.entity_group_

  def mutable_entity_group(self): self.has_entity_group_ = 1; return self.entity_group_

  def clear_entity_group(self):self.has_entity_group_ = 0; self.entity_group_.Clear()

  def has_entity_group(self): return self.has_entity_group_

  def owner(self):
    if self.owner_ is None:
      self.lazy_init_lock_.acquire()
      try:
        if self.owner_ is None: self.owner_ = User()
      finally:
        self.lazy_init_lock_.release()
    return self.owner_

  def mutable_owner(self): self.has_owner_ = 1; return self.owner()

  def clear_owner(self):
    self.has_owner_ = 0;
    if self.owner_ is not None: self.owner_.Clear()

  def has_owner(self): return self.has_owner_

  def kind(self): return self.kind_

  def set_kind(self, x):
    self.has_kind_ = 1
    self.kind_ = x

  def clear_kind(self):
    self.has_kind_ = 0
    self.kind_ = 0

  def has_kind(self): return self.has_kind_

  def kind_uri(self): return self.kind_uri_

  def set_kind_uri(self, x):
    self.has_kind_uri_ = 1
    self.kind_uri_ = x

  def clear_kind_uri(self):
    self.has_kind_uri_ = 0
    self.kind_uri_ = ""

  def has_kind_uri(self): return self.has_kind_uri_

  def property_size(self): return len(self.property_)
  def property_list(self): return self.property_

  def property(self, i):
    return self.property_[i]

  def mutable_property(self, i):
    return self.property_[i]

  def add_property(self):
    x = Property()
    self.property_.append(x)
    return x

  def clear_property(self):
    self.property_ = []
  def raw_property_size(self): return len(self.raw_property_)
  def raw_property_list(self): return self.raw_property_

  def raw_property(self, i):
    return self.raw_property_[i]

  def mutable_raw_property(self, i):
    return self.raw_property_[i]

  def add_raw_property(self):
    x = Property()
    self.raw_property_.append(x)
    return x

  def clear_raw_property(self):
    self.raw_property_ = []

  def MergeFrom(self, x):
    assert x is not self
    if (x.has_key()): self.mutable_key().MergeFrom(x.key())
    if (x.has_entity_group()): self.mutable_entity_group().MergeFrom(x.entity_group())
    if (x.has_owner()): self.mutable_owner().MergeFrom(x.owner())
    if (x.has_kind()): self.set_kind(x.kind())
    if (x.has_kind_uri()): self.set_kind_uri(x.kind_uri())
    for i in xrange(x.property_size()): self.add_property().CopyFrom(x.property(i))
    for i in xrange(x.raw_property_size()): self.add_raw_property().CopyFrom(x.raw_property(i))

  def Equals(self, x):
    if x is self: return 1
    if self.has_key_ != x.has_key_: return 0
    if self.has_key_ and self.key_ != x.key_: return 0
    if self.has_entity_group_ != x.has_entity_group_: return 0
    if self.has_entity_group_ and self.entity_group_ != x.entity_group_: return 0
    if self.has_owner_ != x.has_owner_: return 0
    if self.has_owner_ and self.owner_ != x.owner_: return 0
    if self.has_kind_ != x.has_kind_: return 0
    if self.has_kind_ and self.kind_ != x.kind_: return 0
    if self.has_kind_uri_ != x.has_kind_uri_: return 0
    if self.has_kind_uri_ and self.kind_uri_ != x.kind_uri_: return 0
    if len(self.property_) != len(x.property_): return 0
    for e1, e2 in zip(self.property_, x.property_):
      if e1 != e2: return 0
    if len(self.raw_property_) != len(x.raw_property_): return 0
    for e1, e2 in zip(self.raw_property_, x.raw_property_):
      if e1 != e2: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_key_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: key not set.')
    elif not self.key_.IsInitialized(debug_strs): initialized = 0
    if (not self.has_entity_group_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: entity_group not set.')
    elif not self.entity_group_.IsInitialized(debug_strs): initialized = 0
    if (self.has_owner_ and not self.owner_.IsInitialized(debug_strs)): initialized = 0
    for p in self.property_:
      if not p.IsInitialized(debug_strs): initialized=0
    for p in self.raw_property_:
      if not p.IsInitialized(debug_strs): initialized=0
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthString(self.key_.ByteSize())
    n += self.lengthString(self.entity_group_.ByteSize())
    if (self.has_owner_): n += 2 + self.lengthString(self.owner_.ByteSize())
    if (self.has_kind_): n += 1 + self.lengthVarInt64(self.kind_)
    if (self.has_kind_uri_): n += 1 + self.lengthString(len(self.kind_uri_))
    n += 1 * len(self.property_)
    for i in xrange(len(self.property_)): n += self.lengthString(self.property_[i].ByteSize())
    n += 1 * len(self.raw_property_)
    for i in xrange(len(self.raw_property_)): n += self.lengthString(self.raw_property_[i].ByteSize())
    return n + 3

  def Clear(self):
    self.clear_key()
    self.clear_entity_group()
    self.clear_owner()
    self.clear_kind()
    self.clear_kind_uri()
    self.clear_property()
    self.clear_raw_property()

  def OutputUnchecked(self, out):
    if (self.has_kind_):
      out.putVarInt32(32)
      out.putVarInt32(self.kind_)
    if (self.has_kind_uri_):
      out.putVarInt32(42)
      out.putPrefixedString(self.kind_uri_)
    out.putVarInt32(106)
    out.putVarInt32(self.key_.ByteSize())
    self.key_.OutputUnchecked(out)
    for i in xrange(len(self.property_)):
      out.putVarInt32(114)
      out.putVarInt32(self.property_[i].ByteSize())
      self.property_[i].OutputUnchecked(out)
    for i in xrange(len(self.raw_property_)):
      out.putVarInt32(122)
      out.putVarInt32(self.raw_property_[i].ByteSize())
      self.raw_property_[i].OutputUnchecked(out)
    out.putVarInt32(130)
    out.putVarInt32(self.entity_group_.ByteSize())
    self.entity_group_.OutputUnchecked(out)
    if (self.has_owner_):
      out.putVarInt32(138)
      out.putVarInt32(self.owner_.ByteSize())
      self.owner_.OutputUnchecked(out)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 32:
        self.set_kind(d.getVarInt32())
        continue
      if tt == 42:
        self.set_kind_uri(d.getPrefixedString())
        continue
      if tt == 106:
        length = d.getVarInt32()
        tmp = ProtocolBuffer.Decoder(d.buffer(), d.pos(), d.pos() + length)
        d.skip(length)
        self.mutable_key().TryMerge(tmp)
        continue
      if tt == 114:
        length = d.getVarInt32()
        tmp = ProtocolBuffer.Decoder(d.buffer(), d.pos(), d.pos() + length)
        d.skip(length)
        self.add_property().TryMerge(tmp)
        continue
      if tt == 122:
        length = d.getVarInt32()
        tmp = ProtocolBuffer.Decoder(d.buffer(), d.pos(), d.pos() + length)
        d.skip(length)
        self.add_raw_property().TryMerge(tmp)
        continue
      if tt == 130:
        length = d.getVarInt32()
        tmp = ProtocolBuffer.Decoder(d.buffer(), d.pos(), d.pos() + length)
        d.skip(length)
        self.mutable_entity_group().TryMerge(tmp)
        continue
      if tt == 138:
        length = d.getVarInt32()
        tmp = ProtocolBuffer.Decoder(d.buffer(), d.pos(), d.pos() + length)
        d.skip(length)
        self.mutable_owner().TryMerge(tmp)
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_key_:
      res+=prefix+"key <\n"
      res+=self.key_.__str__(prefix + "  ", printElemNumber)
      res+=prefix+">\n"
    if self.has_entity_group_:
      res+=prefix+"entity_group <\n"
      res+=self.entity_group_.__str__(prefix + "  ", printElemNumber)
      res+=prefix+">\n"
    if self.has_owner_:
      res+=prefix+"owner <\n"
      res+=self.owner_.__str__(prefix + "  ", printElemNumber)
      res+=prefix+">\n"
    if self.has_kind_: res+=prefix+("kind: %s\n" % self.DebugFormatInt32(self.kind_))
    if self.has_kind_uri_: res+=prefix+("kind_uri: %s\n" % self.DebugFormatString(self.kind_uri_))
    cnt=0
    for e in self.property_:
      elm=""
      if printElemNumber: elm="(%d)" % cnt
      res+=prefix+("property%s <\n" % elm)
      res+=e.__str__(prefix + "  ", printElemNumber)
      res+=prefix+">\n"
      cnt+=1
    cnt=0
    for e in self.raw_property_:
      elm=""
      if printElemNumber: elm="(%d)" % cnt
      res+=prefix+("raw_property%s <\n" % elm)
      res+=e.__str__(prefix + "  ", printElemNumber)
      res+=prefix+">\n"
      cnt+=1
    return res

  kkey = 13
  kentity_group = 16
  kowner = 17
  kkind = 4
  kkind_uri = 5
  kproperty = 14
  kraw_property = 15

  _TEXT = (
   "ErrorCode",
   None,
   None,
   None,
   "kind",
   "kind_uri",
   None,
   None,
   None,
   None,
   None,
   None,
   None,
   "key",
   "property",
   "raw_property",
   "entity_group",
   "owner",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
   ProtocolBuffer.Encoder.MAX_TYPE,

   ProtocolBuffer.Encoder.MAX_TYPE,

   ProtocolBuffer.Encoder.MAX_TYPE,

   ProtocolBuffer.Encoder.NUMERIC,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.MAX_TYPE,

   ProtocolBuffer.Encoder.MAX_TYPE,

   ProtocolBuffer.Encoder.MAX_TYPE,

   ProtocolBuffer.Encoder.MAX_TYPE,

   ProtocolBuffer.Encoder.MAX_TYPE,

   ProtocolBuffer.Encoder.MAX_TYPE,

   ProtocolBuffer.Encoder.MAX_TYPE,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.STRING,

  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class CompositeProperty(ProtocolBuffer.ProtocolMessage):
  has_index_id_ = 0
  index_id_ = 0

  def __init__(self, contents=None):
    self.value_ = []
    if contents is not None: self.MergeFromString(contents)

  def index_id(self): return self.index_id_

  def set_index_id(self, x):
    self.has_index_id_ = 1
    self.index_id_ = x

  def clear_index_id(self):
    self.has_index_id_ = 0
    self.index_id_ = 0

  def has_index_id(self): return self.has_index_id_

  def value_size(self): return len(self.value_)
  def value_list(self): return self.value_

  def value(self, i):
    return self.value_[i]

  def set_value(self, i, x):
    self.value_[i] = x

  def add_value(self, x):
    self.value_.append(x)

  def clear_value(self):
    self.value_ = []


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_index_id()): self.set_index_id(x.index_id())
    for i in xrange(x.value_size()): self.add_value(x.value(i))

  def Equals(self, x):
    if x is self: return 1
    if self.has_index_id_ != x.has_index_id_: return 0
    if self.has_index_id_ and self.index_id_ != x.index_id_: return 0
    if len(self.value_) != len(x.value_): return 0
    for e1, e2 in zip(self.value_, x.value_):
      if e1 != e2: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_index_id_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: index_id not set.')
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthVarInt64(self.index_id_)
    n += 1 * len(self.value_)
    for i in xrange(len(self.value_)): n += self.lengthString(len(self.value_[i]))
    return n + 1

  def Clear(self):
    self.clear_index_id()
    self.clear_value()

  def OutputUnchecked(self, out):
    out.putVarInt32(8)
    out.putVarInt64(self.index_id_)
    for i in xrange(len(self.value_)):
      out.putVarInt32(18)
      out.putPrefixedString(self.value_[i])

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 8:
        self.set_index_id(d.getVarInt64())
        continue
      if tt == 18:
        self.add_value(d.getPrefixedString())
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_index_id_: res+=prefix+("index_id: %s\n" % self.DebugFormatInt64(self.index_id_))
    cnt=0
    for e in self.value_:
      elm=""
      if printElemNumber: elm="(%d)" % cnt
      res+=prefix+("value%s: %s\n" % (elm, self.DebugFormatString(e)))
      cnt+=1
    return res

  kindex_id = 1
  kvalue = 2

  _TEXT = (
   "ErrorCode",
   "index_id",
   "value",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
   ProtocolBuffer.Encoder.NUMERIC,

   ProtocolBuffer.Encoder.STRING,

  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class Index_Property(ProtocolBuffer.ProtocolMessage):

  ASCENDING    =    1
  DESCENDING   =    2

  _Direction_NAMES = {
    1: "ASCENDING",
    2: "DESCENDING",
  }

  def Direction_Name(cls, x): return cls._Direction_NAMES.get(x, "")
  Direction_Name = classmethod(Direction_Name)

  has_name_ = 0
  name_ = ""
  has_direction_ = 0
  direction_ = 1

  def __init__(self, contents=None):
    if contents is not None: self.MergeFromString(contents)

  def name(self): return self.name_

  def set_name(self, x):
    self.has_name_ = 1
    self.name_ = x

  def clear_name(self):
    self.has_name_ = 0
    self.name_ = ""

  def has_name(self): return self.has_name_

  def direction(self): return self.direction_

  def set_direction(self, x):
    self.has_direction_ = 1
    self.direction_ = x

  def clear_direction(self):
    self.has_direction_ = 0
    self.direction_ = 1

  def has_direction(self): return self.has_direction_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_name()): self.set_name(x.name())
    if (x.has_direction()): self.set_direction(x.direction())

  def Equals(self, x):
    if x is self: return 1
    if self.has_name_ != x.has_name_: return 0
    if self.has_name_ and self.name_ != x.name_: return 0
    if self.has_direction_ != x.has_direction_: return 0
    if self.has_direction_ and self.direction_ != x.direction_: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_name_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: name not set.')
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthString(len(self.name_))
    if (self.has_direction_): n += 1 + self.lengthVarInt64(self.direction_)
    return n + 1

  def Clear(self):
    self.clear_name()
    self.clear_direction()

  def OutputUnchecked(self, out):
    out.putVarInt32(26)
    out.putPrefixedString(self.name_)
    if (self.has_direction_):
      out.putVarInt32(32)
      out.putVarInt32(self.direction_)

  def TryMerge(self, d):
    while 1:
      tt = d.getVarInt32()
      if tt == 20: break
      if tt == 26:
        self.set_name(d.getPrefixedString())
        continue
      if tt == 32:
        self.set_direction(d.getVarInt32())
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_name_: res+=prefix+("name: %s\n" % self.DebugFormatString(self.name_))
    if self.has_direction_: res+=prefix+("direction: %s\n" % self.DebugFormatInt32(self.direction_))
    return res

class Index(ProtocolBuffer.ProtocolMessage):
  has_entity_type_ = 0
  entity_type_ = ""
  has_ancestor_ = 0
  ancestor_ = 0

  def __init__(self, contents=None):
    self.property_ = []
    if contents is not None: self.MergeFromString(contents)

  def entity_type(self): return self.entity_type_

  def set_entity_type(self, x):
    self.has_entity_type_ = 1
    self.entity_type_ = x

  def clear_entity_type(self):
    self.has_entity_type_ = 0
    self.entity_type_ = ""

  def has_entity_type(self): return self.has_entity_type_

  def ancestor(self): return self.ancestor_

  def set_ancestor(self, x):
    self.has_ancestor_ = 1
    self.ancestor_ = x

  def clear_ancestor(self):
    self.has_ancestor_ = 0
    self.ancestor_ = 0

  def has_ancestor(self): return self.has_ancestor_

  def property_size(self): return len(self.property_)
  def property_list(self): return self.property_

  def property(self, i):
    return self.property_[i]

  def mutable_property(self, i):
    return self.property_[i]

  def add_property(self):
    x = Index_Property()
    self.property_.append(x)
    return x

  def clear_property(self):
    self.property_ = []

  def MergeFrom(self, x):
    assert x is not self
    if (x.has_entity_type()): self.set_entity_type(x.entity_type())
    if (x.has_ancestor()): self.set_ancestor(x.ancestor())
    for i in xrange(x.property_size()): self.add_property().CopyFrom(x.property(i))

  def Equals(self, x):
    if x is self: return 1
    if self.has_entity_type_ != x.has_entity_type_: return 0
    if self.has_entity_type_ and self.entity_type_ != x.entity_type_: return 0
    if self.has_ancestor_ != x.has_ancestor_: return 0
    if self.has_ancestor_ and self.ancestor_ != x.ancestor_: return 0
    if len(self.property_) != len(x.property_): return 0
    for e1, e2 in zip(self.property_, x.property_):
      if e1 != e2: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_entity_type_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: entity_type not set.')
    if (not self.has_ancestor_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: ancestor not set.')
    for p in self.property_:
      if not p.IsInitialized(debug_strs): initialized=0
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthString(len(self.entity_type_))
    n += 2 * len(self.property_)
    for i in xrange(len(self.property_)): n += self.property_[i].ByteSize()
    return n + 3

  def Clear(self):
    self.clear_entity_type()
    self.clear_ancestor()
    self.clear_property()

  def OutputUnchecked(self, out):
    out.putVarInt32(10)
    out.putPrefixedString(self.entity_type_)
    for i in xrange(len(self.property_)):
      out.putVarInt32(19)
      self.property_[i].OutputUnchecked(out)
      out.putVarInt32(20)
    out.putVarInt32(40)
    out.putBoolean(self.ancestor_)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 10:
        self.set_entity_type(d.getPrefixedString())
        continue
      if tt == 19:
        self.add_property().TryMerge(d)
        continue
      if tt == 40:
        self.set_ancestor(d.getBoolean())
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_entity_type_: res+=prefix+("entity_type: %s\n" % self.DebugFormatString(self.entity_type_))
    if self.has_ancestor_: res+=prefix+("ancestor: %s\n" % self.DebugFormatBool(self.ancestor_))
    cnt=0
    for e in self.property_:
      elm=""
      if printElemNumber: elm="(%d)" % cnt
      res+=prefix+("Property%s {\n" % elm)
      res+=e.__str__(prefix + "  ", printElemNumber)
      res+=prefix+"}\n"
      cnt+=1
    return res

  kentity_type = 1
  kancestor = 5
  kPropertyGroup = 2
  kPropertyname = 3
  kPropertydirection = 4

  _TEXT = (
   "ErrorCode",
   "entity_type",
   "Property",
   "name",
   "direction",
   "ancestor",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.STARTGROUP,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.NUMERIC,

   ProtocolBuffer.Encoder.NUMERIC,

  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""
class CompositeIndex(ProtocolBuffer.ProtocolMessage):

  WRITE_ONLY   =    1
  READ_WRITE   =    2
  DELETED      =    3
  ERROR        =    4

  _State_NAMES = {
    1: "WRITE_ONLY",
    2: "READ_WRITE",
    3: "DELETED",
    4: "ERROR",
  }

  def State_Name(cls, x): return cls._State_NAMES.get(x, "")
  State_Name = classmethod(State_Name)

  has_app_id_ = 0
  app_id_ = ""
  has_id_ = 0
  id_ = 0
  has_definition_ = 0
  has_state_ = 0
  state_ = 0

  def __init__(self, contents=None):
    self.definition_ = Index()
    if contents is not None: self.MergeFromString(contents)

  def app_id(self): return self.app_id_

  def set_app_id(self, x):
    self.has_app_id_ = 1
    self.app_id_ = x

  def clear_app_id(self):
    self.has_app_id_ = 0
    self.app_id_ = ""

  def has_app_id(self): return self.has_app_id_

  def id(self): return self.id_

  def set_id(self, x):
    self.has_id_ = 1
    self.id_ = x

  def clear_id(self):
    self.has_id_ = 0
    self.id_ = 0

  def has_id(self): return self.has_id_

  def definition(self): return self.definition_

  def mutable_definition(self): self.has_definition_ = 1; return self.definition_

  def clear_definition(self):self.has_definition_ = 0; self.definition_.Clear()

  def has_definition(self): return self.has_definition_

  def state(self): return self.state_

  def set_state(self, x):
    self.has_state_ = 1
    self.state_ = x

  def clear_state(self):
    self.has_state_ = 0
    self.state_ = 0

  def has_state(self): return self.has_state_


  def MergeFrom(self, x):
    assert x is not self
    if (x.has_app_id()): self.set_app_id(x.app_id())
    if (x.has_id()): self.set_id(x.id())
    if (x.has_definition()): self.mutable_definition().MergeFrom(x.definition())
    if (x.has_state()): self.set_state(x.state())

  def Equals(self, x):
    if x is self: return 1
    if self.has_app_id_ != x.has_app_id_: return 0
    if self.has_app_id_ and self.app_id_ != x.app_id_: return 0
    if self.has_id_ != x.has_id_: return 0
    if self.has_id_ and self.id_ != x.id_: return 0
    if self.has_definition_ != x.has_definition_: return 0
    if self.has_definition_ and self.definition_ != x.definition_: return 0
    if self.has_state_ != x.has_state_: return 0
    if self.has_state_ and self.state_ != x.state_: return 0
    return 1

  def __eq__(self, other):
    return (other is not None) and (other.__class__ == self.__class__) and self.Equals(other)

  def __ne__(self, other):
    return not (self == other)

  def IsInitialized(self, debug_strs=None):
    initialized = 1
    if (not self.has_app_id_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: app_id not set.')
    if (not self.has_id_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: id not set.')
    if (not self.has_definition_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: definition not set.')
    elif not self.definition_.IsInitialized(debug_strs): initialized = 0
    if (not self.has_state_):
      initialized = 0
      if debug_strs is not None:
        debug_strs.append('Required field: state not set.')
    return initialized

  def ByteSize(self):
    n = 0
    n += self.lengthString(len(self.app_id_))
    n += self.lengthVarInt64(self.id_)
    n += self.lengthString(self.definition_.ByteSize())
    n += self.lengthVarInt64(self.state_)
    return n + 4

  def Clear(self):
    self.clear_app_id()
    self.clear_id()
    self.clear_definition()
    self.clear_state()

  def OutputUnchecked(self, out):
    out.putVarInt32(10)
    out.putPrefixedString(self.app_id_)
    out.putVarInt32(16)
    out.putVarInt64(self.id_)
    out.putVarInt32(26)
    out.putVarInt32(self.definition_.ByteSize())
    self.definition_.OutputUnchecked(out)
    out.putVarInt32(32)
    out.putVarInt32(self.state_)

  def TryMerge(self, d):
    while d.avail() > 0:
      tt = d.getVarInt32()
      if tt == 10:
        self.set_app_id(d.getPrefixedString())
        continue
      if tt == 16:
        self.set_id(d.getVarInt64())
        continue
      if tt == 26:
        length = d.getVarInt32()
        tmp = ProtocolBuffer.Decoder(d.buffer(), d.pos(), d.pos() + length)
        d.skip(length)
        self.mutable_definition().TryMerge(tmp)
        continue
      if tt == 32:
        self.set_state(d.getVarInt32())
        continue
      if (tt == 0): raise ProtocolBuffer.ProtocolBufferDecodeError
      d.skipData(tt)


  def __str__(self, prefix="", printElemNumber=0):
    res=""
    if self.has_app_id_: res+=prefix+("app_id: %s\n" % self.DebugFormatString(self.app_id_))
    if self.has_id_: res+=prefix+("id: %s\n" % self.DebugFormatInt64(self.id_))
    if self.has_definition_:
      res+=prefix+"definition <\n"
      res+=self.definition_.__str__(prefix + "  ", printElemNumber)
      res+=prefix+">\n"
    if self.has_state_: res+=prefix+("state: %s\n" % self.DebugFormatInt32(self.state_))
    return res

  kapp_id = 1
  kid = 2
  kdefinition = 3
  kstate = 4

  _TEXT = (
   "ErrorCode",
   "app_id",
   "id",
   "definition",
   "state",
  )

  _TYPES = (
   ProtocolBuffer.Encoder.NUMERIC,
   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.NUMERIC,

   ProtocolBuffer.Encoder.STRING,

   ProtocolBuffer.Encoder.NUMERIC,

  )

  _STYLE = """"""
  _STYLE_CONTENT_TYPE = """"""

__all__ = ['PropertyValue','PropertyValue_ReferenceValuePathElement','PropertyValue_PointValue','PropertyValue_UserValue','PropertyValue_ReferenceValue','Property','Path','Path_Element','Reference','User','EntityProto','CompositeProperty','Index','Index_Property','CompositeIndex']
