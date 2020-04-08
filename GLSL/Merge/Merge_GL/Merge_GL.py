# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named Merge_GLExt.py
# See http://natron.readthedocs.org/en/master/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from Merge_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.Merge_GL"

def getLabel():
    return "Merge_GL"

def getVersion():
    return 1

def getIconPath():
    return "Merge_GL.png"

def getGrouping():
    return "Community/GLSL/Merge"

def getPluginDescription():
    return "GPU accelerated merge node for Shadertoy."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.2941, 0.3686, 0.7765)

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Merge_GL")
    param = lastNode.createStringParam("sep01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep01 = param
    del param

    param = lastNode.createStringParam("sep02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep02 = param
    del param

    param = lastNode.createChoiceParam("blending", "Operation")
    entries = [ ("colorBurn", ""),
    ("colorDodge", ""),
    ("darken", ""),
    ("darkerColor", ""),
    ("difference", ""),
    ("divide", ""),
    ("exclusion", ""),
    ("hardLight", ""),
    ("hardMix", ""),
    ("lighten", ""),
    ("lighterColor", ""),
    ("linearBurn", ""),
    ("linearDodge", ""),
    ("linearLight", ""),
    ("luminosity", ""),
    ("matte", ""),
    ("multiply", ""),
    ("over", ""),
    ("overlay", ""),
    ("pinLight", ""),
    ("plus", ""),
    ("screen", ""),
    ("softLight", ""),
    ("spotlightBlend", ""),
    ("substract", ""),
    ("vividLight", "")]
    param.setOptions(entries)
    del entries
    param.setDefaultValue("over")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    lastNode.blending = param
    del param

    param = lastNode.createStringParam("sep03", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep03 = param
    del param

    param = lastNode.createStringParam("sep04", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep04 = param
    del param

    param = lastNode.createSeparatorParam("line01", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line01 = param
    del param

    param = lastNode.createStringParam("aChannels", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("A Channels")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.aChannels = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool2", "R")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool2 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool3", "G")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool3 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool4", "B")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool4 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool5", "A")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool5 = param
    del param

    param = lastNode.createStringParam("bChannels", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)
    param.setDefaultValue("B Channels")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.bChannels = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool6", "R")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool6 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool7", "G")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool7 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool8", "B")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool8 = param
    del param

    param = lastNode.createBooleanParam("Shadertoy1_2paramValueBool9", "A")
    param.setDefaultValue(True)
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(False)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueBool9 = param
    del param

    param = lastNode.createSeparatorParam("line02", "")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line02 = param
    del param

    param = lastNode.createDoubleParam("Shadertoy1_2paramValueFloat1", "Mix :")
    param.setMinimum(0, 0)
    param.setMaximum(1, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueFloat1 = param
    del param

    param = lastNode.createStringParam("sep05", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep05 = param
    del param

    param = lastNode.createStringParam("sep06", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep06 = param
    del param

    param = lastNode.createStringParam("sep07", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep07 = param
    del param

    param = lastNode.createStringParam("sep08", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep08 = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("separator19", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator19 = param
    del param

    param = lastNode.createStringParam("separator20", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator20 = param
    del param

    param = lastNode.createSeparatorParam("line03", "Merge_GL v1.0")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line03 = param
    del param

    param = lastNode.createStringParam("separator21", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator21 = param
    del param

    param = lastNode.createStringParam("separator22", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator22 = param
    del param

    param = lastNode.createSeparatorParam("line04", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.line04 = param
    del param

    param = lastNode.createStringParam("separator23", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator23 = param
    del param

    param = lastNode.createStringParam("separator24", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator24 = param
    del param

    param = lastNode.createSeparatorParam("FR", "ShaderToy 0.8.8")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FR = param
    del param

    param = lastNode.createStringParam("separator25", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator25 = param
    del param

    param = lastNode.createStringParam("separator26", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator26 = param
    del param

    param = lastNode.createSeparatorParam("conversion", " (Fabrice Fernandez - 2018)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.conversion = param
    del param

    param = lastNode.createStringParam("separator27", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator27 = param
    del param

    param = lastNode.createStringParam("separator28", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.separator28 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output2"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output2")
    lastNode.setPosition(4139, 4048)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput2 = lastNode

    del lastNode
    # End of node "Output2"

    # Start of node "B"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("B")
    lastNode.setLabel("B")
    lastNode.setPosition(4139, 3647)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupB = lastNode

    del lastNode
    # End of node "B"

    # Start of node "A"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("A")
    lastNode.setLabel("A")
    lastNode.setPosition(4334, 3813)
    lastNode.setSize(80, 43)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupA = lastNode

    del lastNode
    # End of node "A"

    # Start of node "Shadertoy1_2"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy1_2")
    lastNode.setLabel("Shadertoy1_2")
    lastNode.setPosition(4139, 3810)
    lastNode.setSize(80, 48)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy1_2 = lastNode

    param = lastNode.getParam("paramValueInt0")
    if param is not None:
        param.setValue(17, 0)
        del param

    param = lastNode.getParam("paramValueFloat1")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramValueBool2")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool3")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool4")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool5")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool6")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool7")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool8")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueBool9")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("""//                                                
//
//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM
//                        MM.                          .MM
//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM
//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM
//                     MM.  .MMMM        MMMMMMM    MMM.  .MM
//                    MM.  .MMM           MMMMMM     MMM.  .MM
//                   MM.  .MmM              MMMM      MMM.  .MM
//                  MM.  .MMM                 MM       MMM.  .MM
//                 MM.  .MMM                   M        MMM.  .MM
//                MM.  .MMM                              MMM.  .MM
//                 MM.  .MMM                            MMM.  .MM
//                  MM.  .MMM       M                  MMM.  .MM
//                   MM.  .MMM      MM                MMM.  .MM
//                    MM.  .MMM     MMM              MMM.  .MM
//                     MM.  .MMM    MMMM            MMM.  .MM
//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM
//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM
//                        MM.                          .MM
//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM
//
//
// Adaptation pour Natron par F. Fernandez
// Code original : crok_logicop Matchbox pour Autodesk Flame
//
// Adapted to Natron by F.Fernandez
// Original code : crok_logicop Matchbox for Autodesk Flame
//
//****************************************************************************/
//
// Filename: logicOPS_3vis.glsl
// Author: Eric Pouliot
//
// Copyright (c) 2013 3vis, Inc.
//
//*****************************************************************************/
//
//  License Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
//
//  25 of the layer blending modes from Photoshop.
//
//  The ones I couldn't figure out are from Nvidia's advanced blend equations extension spec -
//  http://www.opengl.org/registry/specs/NV/blend_equation_advanced.txt
//
//  ~bj.2013
//
//*****************************************************************************/

// iChannel0: B, filter = nearest
// iChannel1: A, filter = nearest
// iChannel1: Modulate, filter = nearest
// BBox: iChannel0


const vec2 iChannelOffset[4] = vec2[4]( vec2(0.,0.), vec2(0.,0.), vec2(0.,0.), vec2(0.,0.) );

uniform int blendingMode = 17; // Operation : (blending mode), min=0., max=25.
uniform float opacity = 1; // Mix : (mix), min=0., max=1.

uniform bool Ar = true; // R
uniform bool Ag = true; // G
uniform bool Ab = true; // B
uniform bool Aa = true; // A

uniform bool Br = true; // R
uniform bool Bg = true; // G
uniform bool Bb = true; // B
uniform bool Ba = true; // A


//********************* fonctions ***********************//

float overlay( float s, float d )
{
  return (d < 0.5) ? 2.0 * s * d : 1.0 - 2.0 * (1.0 - s) * (1.0 - d);
}

float softLight( float s, float d )
{
  return (s < 0.5) ? d - (1.0 - 2.0 * s) * d * (1.0 - d)
    : (d < 0.25) ? d + (2.0 * s - 1.0) * d * ((16.0 * d - 12.0) * d + 3.0)
           : d + (2.0 * s - 1.0) * (sqrt(d) - d);
}

float hardLight( float s, float d )
{
  return (s < 0.5) ? 2.0 * s * d : 1.0 - 2.0 * (1.0 - s) * (1.0 - d);
}

float vividLight( float s, float d )
{
  return (s < 0.5) ? 1.0 - (1.0 - d) / (2.0 * s) : d / (2.0 * (1.0 - s));
}

float pinLight( float s, float d )
{
  return (2.0 * s - 1.0 > d) ? 2.0 * s - 1.0 : (s < 0.5 * d) ? 2.0 * s : d;
}



//****************** modes de fusion ********************//

vec4 colorBurn( vec4 s, vec4 d )
{
  return 1.0 - (1.0 - d) / s;
}

vec4 colorDodge( vec4 s, vec4 d )
{
  return d / (1.0 - s);
}

vec4 darken( vec4 s, vec4 d )
{
  vec4 c;
  c = min(s,d);
  return c;
}

vec4 difference( vec4 s, vec4 d )
{
  return abs(d - s);
}

vec4 darkerColor( vec4 s, vec4 d )
{
  return (s.x + s.y + s.z < d.x + d.y + d.z) ? s : d;
}

vec4 divide( vec4 s, vec4 d )
{
  return s / d;
}

vec4 exclusion( vec4 s, vec4 d )
{
  return s + d - 2.0 * s * d;
}

vec4 hardLight( vec4 s, vec4 d )
{
  vec4 c;
  c.x = hardLight(s.x,d.x);
  c.y = hardLight(s.y,d.y);
  c.z = hardLight(s.z,d.z);
  return c;
}

vec4 hardMix( vec4 s, vec4 d )
{
  return floor(s + d);
}

vec4 lighten( vec4 s, vec4 d )
{
  return max(s,d);
}

vec4 lighterColor( vec4 s, vec4 d )
{
  return (s.x + s.y + s.z > d.x + d.y + d.z) ? s : d;
}

vec4 linearBurn( vec4 s, vec4 d )
{
  return s + d - 1.0;
}

vec4 linearDodge( vec4 s, vec4 d )
{
  return s + d;
}


vec4 linearLight( vec4 s, vec4 d )
{
  return 2.0 * s + d - 1.0;
}

vec4 screen( vec4 s, vec4 d )
{
  return s + d - s * d;
}

vec4 screenMode( vec4 s, vec4 d )
{
  vec4 c;
  c = 1 - (1 - s) * (1 - d);
  return c;
}

vec4 matte( vec4 s, vec4 d)
{
  vec4 c = vec4(0,0,0,0);
  c = (s*s.a) + (d*(1-s.a));
  c.a = s.a;
  return c;
}

vec4 multiply( vec4 s, vec4 d )
{
  return s*d;
}

vec4 overlay( vec4 s, vec4 d )
{
  vec4 c;
  c.x = overlay(s.x,d.x);
  c.y = overlay(s.y,d.y);
  c.z = overlay(s.z,d.z);
  return c;
}

vec4 pinLight( vec4 s, vec4 d )
{
  vec4 c;
  c.x = pinLight(s.x,d.x);
  c.y = pinLight(s.y,d.y);
  c.z = pinLight(s.z,d.z);
  return c;
}

vec4 plus( vec4 s, vec4 d )
{
  return s + d;
}

vec4 softLight( vec4 s, vec4 d )
{
  vec4 c;
  c.x = softLight(s.x,d.x);
  c.y = softLight(s.y,d.y);
  c.z = softLight(s.z,d.z);
  return c;
}

vec4 spotlightBlend( vec4 s, vec4 d )
{
  return d*s+d;
}

vec4 substract( vec4 s, vec4 d )
{
  return s - d;
}

vec4 vividLight( vec4 s, vec4 d )
{
  vec4 c;
  c.x = vividLight(s.x,d.x);
  c.y = vividLight(s.y,d.y);
  c.z = vividLight(s.z,d.z);
  return c;
}

vec4 luminosity( vec4 s, vec4 d )
{
  float dLum = dot(d, vec4(0.3, 0.59, 0.11,0));
  float sLum = dot(s, vec4(0.3, 0.59, 0.11,0));
  float lum = sLum - dLum;
  vec4 c = d + lum;
  float minC = min(min(c.x, c.y), c.z);
  float maxC = max(max(c.x, c.y), c.z);
  if(minC < 0.0) return sLum + ((c - sLum) * sLum) / (sLum - minC);
  else if(maxC > 1.0) return sLum + ((c - sLum) * (1.0 - sLum)) / (maxC - sLum);
  else return c;
}

vec4 over( vec4 s, vec4 d )
{
  vec4 c;
  c = s + ( d*(1-s.a) );
  return c;
}


void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
  // source texture (upper layer)
  vec4 s = texture2D(iChannel1, (fragCoord.xy-iChannelOffset[1].xy)/iChannelResolution[1].xy);

  // destination texture (lower layer)
  vec4 d = texture2D(iChannel0, fragCoord.xy / iChannelResolution[0].xy);

  // mask texture (mask entry)
  vec4 mask = texture2D(iChannel2, (fragCoord.xy-iChannelOffset[2].xy)/iChannelResolution[2].xy);

  vec4 c = vec4(0.0);


  // ########### selection des couches ########### //

  if(Ar == false)
    s.r = 0;

  if(Ag == false)
    s.g = 0;

  if(Ab == false)
    s.b = 0;

  if(Aa == false)
    s.a = 0;

  if(Br == false)
    d.r = 0;

  if(Bg == false)
    d.g = 0;

  if(Bb == false)
    d.b = 0;

  if(Ba == false)
    d.a = 0;

  // ########### selection des modes de fusion ########### //

  if( blendingMode == 0)
    c =  c + colorBurn(s,d);

  else if( blendingMode == 1)
    c =  c + colorDodge(s,d);

  else if( blendingMode == 2)
    c =  c + darken(s,d);

  else if(blendingMode == 3)
    c =  c + darkerColor(s,d);

  else if(blendingMode == 4)
    c =  c + difference(s,d);

  else if(blendingMode == 5)
    c =  c + divide(s,d);

  else if(blendingMode == 6)
    c =  c + exclusion(s,d);

  else if(blendingMode == 7)
    c =  c + hardLight(s,d);

  else if(blendingMode == 8)
    c =  c + hardMix(s,d);

  else if(blendingMode == 9)
    c =  c + lighten(s,d);

  else if(blendingMode == 10)
    c =  c + lighterColor(s,d);

  else if(blendingMode == 11)
    c =  c + linearBurn(s,d);

  else if(blendingMode == 12)
    c =  c + linearDodge(s,d);

  else if(blendingMode == 13)
    c =  c + linearLight(s,d);

  else if(blendingMode == 14)
    c =  c + luminosity(s,d);

  else if(blendingMode == 15)
    c =  c + matte(s,d);

  else if(blendingMode == 16)
    c =  c + multiply(s,d);

  else if(blendingMode == 17)
    c =  c + over(s,d);

  else if(blendingMode == 18)
    c =  c + overlay(s,d);

  else if(blendingMode == 19)
    c =  c + pinLight(s,d);

  else if(blendingMode == 20)
    c =  c + plus(s,d);

  else if(blendingMode == 21)
    c =  c + screenMode(s,d);

  else if(blendingMode == 22)
    c =  c + softLight(s,d);

  else if(blendingMode == 23)
    c =  c + spotlightBlend(s,d);

  else if(blendingMode == 24)
    c =  c + substract(s,d);

  else if(blendingMode == 25)
    c =  c + vividLight(s,d);

  // grabbing the result
  vec4 result = vec4(c.rgb, s.a);

  // multiplying the result by the opacity
  fragColor = mix(d, result, opacity);
}""")
        del param

    param = lastNode.getParam("mipmap0")
    if param is not None:
        param.set("nearest")
        del param

    param = lastNode.getParam("inputLabel0")
    if param is not None:
        param.setValue("B")
        del param

    param = lastNode.getParam("mipmap1")
    if param is not None:
        param.set("nearest")
        del param

    param = lastNode.getParam("inputLabel1")
    if param is not None:
        param.setValue("A")
        del param

    param = lastNode.getParam("inputEnable2")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("iChannel0")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(10, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("blendingMode")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Operation :")
        del param

    param = lastNode.getParam("paramHint0")
    if param is not None:
        param.setValue("blending mode")
        del param

    param = lastNode.getParam("paramDefaultInt0")
    if param is not None:
        param.setValue(17, 0)
        del param

    param = lastNode.getParam("paramMinInt0")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxInt0")
    if param is not None:
        param.setValue(25, 0)
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("float")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("opacity")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Mix :")
        del param

    param = lastNode.getParam("paramHint1")
    if param is not None:
        param.setValue("mix")
        del param

    param = lastNode.getParam("paramDefaultFloat1")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramMinFloat1")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxFloat1")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("Ar")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("R")
        del param

    param = lastNode.getParam("paramDefaultBool2")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramType3")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName3")
    if param is not None:
        param.setValue("Ag")
        del param

    param = lastNode.getParam("paramLabel3")
    if param is not None:
        param.setValue("G")
        del param

    param = lastNode.getParam("paramDefaultBool3")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramType4")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName4")
    if param is not None:
        param.setValue("Ab")
        del param

    param = lastNode.getParam("paramLabel4")
    if param is not None:
        param.setValue("B")
        del param

    param = lastNode.getParam("paramDefaultBool4")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramType5")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName5")
    if param is not None:
        param.setValue("Aa")
        del param

    param = lastNode.getParam("paramLabel5")
    if param is not None:
        param.setValue("A")
        del param

    param = lastNode.getParam("paramDefaultBool5")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramType6")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName6")
    if param is not None:
        param.setValue("Br")
        del param

    param = lastNode.getParam("paramLabel6")
    if param is not None:
        param.setValue("R")
        del param

    param = lastNode.getParam("paramDefaultBool6")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramType7")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName7")
    if param is not None:
        param.setValue("Bg")
        del param

    param = lastNode.getParam("paramLabel7")
    if param is not None:
        param.setValue("G")
        del param

    param = lastNode.getParam("paramDefaultBool7")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramType8")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName8")
    if param is not None:
        param.setValue("Bb")
        del param

    param = lastNode.getParam("paramLabel8")
    if param is not None:
        param.setValue("B")
        del param

    param = lastNode.getParam("paramDefaultBool8")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramType9")
    if param is not None:
        param.set("bool")
        del param

    param = lastNode.getParam("paramName9")
    if param is not None:
        param.setValue("Ba")
        del param

    param = lastNode.getParam("paramLabel9")
    if param is not None:
        param.setValue("A")
        del param

    param = lastNode.getParam("paramDefaultBool9")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Shadertoy1_2"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput2.connectInput(0, groupShadertoy1_2)
    groupShadertoy1_2.connectInput(0, groupB)
    groupShadertoy1_2.connectInput(1, groupA)

    param = groupShadertoy1_2.getParam("paramValueInt0")
    param.setExpression("thisGroup.blending.get()", False, 0)
    del param
    param = groupShadertoy1_2.getParam("paramValueFloat1")
    group.getParam("Shadertoy1_2paramValueFloat1").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool2")
    group.getParam("Shadertoy1_2paramValueBool2").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool3")
    group.getParam("Shadertoy1_2paramValueBool3").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool4")
    group.getParam("Shadertoy1_2paramValueBool4").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool5")
    group.getParam("Shadertoy1_2paramValueBool5").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool6")
    group.getParam("Shadertoy1_2paramValueBool6").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool7")
    group.getParam("Shadertoy1_2paramValueBool7").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool8")
    group.getParam("Shadertoy1_2paramValueBool8").setAsAlias(param)
    del param
    param = groupShadertoy1_2.getParam("paramValueBool9")
    group.getParam("Shadertoy1_2paramValueBool9").setAsAlias(param)
    del param

    try:
        extModule = sys.modules["Merge_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
